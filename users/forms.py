from django import forms
from .models import User, UserProgrammingLanguage, EXPERIENCE_CHOICES, LANGUAGE_CHOICES
from django.core.validators import MinLengthValidator
from django.forms import modelformset_factory

class UserProfileSetUpForm( forms.Form ):
    display_name = forms.CharField(max_length=20, validators=[MinLengthValidator(3, message="Display Name should be atleast 3 characters.")])
    skills = forms.CharField(widget=forms.Textarea)
    goals = forms.CharField(widget=forms.Textarea)
    experience_level = forms.ChoiceField(choices=EXPERIENCE_CHOICES)
    languages = forms.MultipleChoiceField(choices=LANGUAGE_CHOICES, widget=forms.SelectMultiple)

