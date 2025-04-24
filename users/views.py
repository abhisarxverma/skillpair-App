from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import *


def index(request):
    return render(request, "users/profile.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "auth/login.html", {
                "errors": "Invalid username and/or password."
            })
    else:
        return render(request, "auth/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("users:login"))

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        # Ensure passwords match
        if password != confirmation:
            return render(request, "auth/register.html", {
                "errors": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
        except IntegrityError:
            return render(request, "auth/register.html", {
                "errors": "Username already taken."
            })

        # Authenticate the user before login
        authenticated_user = authenticate(request, username=username, password=password)
        if authenticated_user:
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse("courses:index"))
        else:
            return render(request, "auth/register.html", {
                "errors": "User created but authentication failed."
            })

    else:
        return render(request, "auth/register.html")
