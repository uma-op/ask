from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import loader

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    template = loader.get_template('signup/signup.html')
    return HttpResponse(template.render(dict(), request))

def param(request: HttpRequest, id: int) -> HttpResponse:
    return HttpResponse(f"You passed {id}")