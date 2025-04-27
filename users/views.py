from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . import forms

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
                "error_message": "Invalid username and/or password."
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
                "error_message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
        except IntegrityError:
            return render(request, "auth/register.html", {
                "error_message": "Username already taken."
            })

        # Authenticate the user before login
        authenticated_user = authenticate(request, username=username, password=password)
        if authenticated_user:
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse("users:profile_setup"))
        else:
            return render(request, "auth/register.html", {
                "errors": "User created but authentication failed."
            })

    else:
        return render(request, "auth/register.html")

@login_required
def profile_setup(request):
    if request.method == 'POST':
        display_name = request.POST.get('display_name', '')
        skills = request.POST.get('skills', '')
        goals = request.POST.get('goals', '')
        experience_level = request.POST.get('experience_level', '')

        # Retrieving selected programming languages
        selected_languages = request.POST.getlist('languages')  # Returns a list

        # Retrieving proficiency scores for languages
        language_proficiency = {lang: int(request.POST.get(lang, '1')) for lang in selected_languages}
        user_profile = UserProfile.objects.create(
            user=request.user,
            display_name=display_name,
            skills=skills,
            goals=goals,
            experience_level=experience_level
        )

        try:
            user_profile.save()
            for lang, pro in language_proficiency.items():
                UserProgrammingLanguage.objects.create(user=request.user, language=lang, proficiency_level=pro).save()

        except Exception as e:
            return render(request, "users/profile_setup.html", {"error_messages" : e})

        # Redirect after successful submission
        return redirect('courses:index')

    return render(request, 'users/profile_setup.html')