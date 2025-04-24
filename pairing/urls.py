from django.urls import path
from . import views

app_name = "pairing"

urlpatterns = [
    path("", views.index, name="index")
]