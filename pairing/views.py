from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    courses = Course.objects.all()
    return render(request, "pairing/pairing_dashboard.html", {
        "courses" : courses
    })