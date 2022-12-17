from django.shortcuts import render

from django.template import loader

from django.http import HttpRequest, HttpResponse

class Error:
    status = 0
    details = ""

    def __init__(self, status, details="") -> None:
        self.status = status
        self.details = details

    def __bool__(self) -> bool:
        return self.status != 0;

def signup(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("signup/signup.html")
    context = { "nickname": "Uma_op", "error": Error(1, "cringe")}
    return HttpResponse(template.render(context, request))

def signin(request: HttpRequest) -> HttpResponse:
    return HttpResponse("not implemented")

def questions(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("questions/")
    return HttpResponse("not implemented")

def question(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse("not implemented")

def ask(request: HttpRequest) -> HttpResponse:
    return HttpResponse("not implemented")

def tag(request: HttpRequest, tag_name: str) -> HttpResponse:
    return HttpResponse("not implemented")

def settings(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("settings/settings.html")
    context = { "nickname": "Uma_op" }
    return HttpResponse(template.render(context, request))
