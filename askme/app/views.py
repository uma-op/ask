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

class Question:  # заглушка для верстки
    author = "ва зеленский"
    theme = "хто я?"
    text = "президент украины!!!"

    def __init__(
        self,
        author="ва зеленский",
        theme="хто я?",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        "Proin ac dapibus dolor."
        "Ut quis tempor odio, at fringilla sem."
        "Sed tincidunt augue quis lacus laoreet, id facilisis sapien auctor."
        "Aenean mattis tempor quam."
        "Suspendisse ultrices nisl tortor, et iaculis leo mattis quis."
        "Sed tempor nulla nec felis dapibus pulvinar."
        "Sed aliquam fringilla sem a finibus."
        "Proin viverra diam erat, commodo tempor justo laoreet sed."
        "Ut semper faucibus rhoncus."
        "Sed tristique arcu at tortor posuere pellentesque."
        "Maecenas ac tortor at mauris dapibus pulvinar ac nec nibh."
        "Etiam eleifend accumsan mi, ut posuere orci aliquet facilisis."
    ) -> None:
        self.author = author
        self.theme = theme
        self.text = text

def signup(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("signup/signup.html")
    context = { "nickname": "Uma_op", "error": Error(1, "some signing up error")}
    return HttpResponse(template.render(context, request))

def signin(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("signin/signin.html")
    context = { "error": Error(1, "some signing in error") }
    return HttpResponse(template.render(context, request))

def questions(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("questions/questions.html")
    context = { "questions_list": [Question("uma_op", "я гуль?"), Question()] }
    return HttpResponse(template.render(context, request))

def question(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse("not implemented")

def ask(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("ask/ask.html")
    context = { "": "" }
    return HttpResponse(template.render(context, request))

def tag(request: HttpRequest, tag_name: str) -> HttpResponse:
    return HttpResponse("not implemented")

def settings(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("settings/settings.html")
    context = { "nickname": "Uma_op", "error": Error(1, "some settings troubles") }
    return HttpResponse(template.render(context, request))
