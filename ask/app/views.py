from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('app/new_questions.html')
    context = dict()
    return HttpResponse(template.render(context, request))

def ask(request):
    template = loader.get_template('app/ask.html')
    context = dict()
    return HttpResponse(template.render(context, request))

def settings(request):
    template = loader.get_template('app/settings.html')
    context = dict()
    return HttpResponse(template.render(context, request))

