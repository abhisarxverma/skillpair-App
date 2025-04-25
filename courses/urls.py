from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path("", views.index, name="index"),
    path("get_all_courses", views.get_all_courses, name="get_all_courses")
]