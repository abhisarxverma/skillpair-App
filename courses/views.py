from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json
# Create your views here.

def index(request):
    return render(request, "courses/courses.html")

def get_all_courses(request):
    all_courses = Course.objects.all()
    all_courses = [ course.serialize() for course in all_courses ]
    response = {
        "success" : True,
        "message" : "Fetched all courses successfully.",
        "courses" : all_courses
    }
    return JsonResponse(response, status=201)