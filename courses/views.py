from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import json
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def index(request, course_id):
    course_data = json.loads(open(os.path.join(BASE_DIR, 'courses.json'),'r').read())
    course_name = course_data[course_id]['name']
    course_description = course_data[course_id]['description']
    course_grades = str(json.dumps(course_data[course_id]['grades']))
    return HttpResponse(render(request, 'course_page.html', context = {'course_id': course_id, 'course_name': course_name, 'grades': course_grades,'course_description':course_description}))

def search(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        print(query)
        subject_id, subject_name = str(query).split('-')
        subject_id = re.findall('[A-Z0-9]+', subject_id)[0]
        return HttpResponseRedirect('/courses/{}'.format(subject_id))
    return HttpResponse(render(request, 'course_search.html'))

def compare(request):
    course_data = json.loads(open(os.path.join(BASE_DIR, 'grades.json'),'r').read())
    course_grades1 = str(json.dumps(course_data['BT21002']['grades']))
    course_grades2 = str(json.dumps(course_data['AG31003']['grades']))
    return HttpResponse(render(request, 'compare_grades.html', context = {'grades1': course_grades1, 'grades2': course_grades2}))
