from django import forms
from django.db.models.expressions import fields

from .models import Answer, Profile, Question

class LoginForm(forms.Form):
    login = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", min_length=6, widget=forms.PasswordInput)
    repeat_password = forms.CharField(label="Repeat password", min_length=6, widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ["login", "email", "nickname", "password", "repeat_password"]

class AskForm(forms.ModelForm):
    tags = forms.CharField()

    class Meta:
        model = Question
        fields = ["theme", "text", "tags"]

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["text"]
        labels = {
            "text": ""
        }

