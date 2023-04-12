from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from django.contrib.auth.models import User

from app.models import Profile, Tag, Question, Answer, QuestionMark, AnswerMark 

class Error:
    def __init__(self, status, details="") -> None:
        self.status = status
        self.details = details

    def __bool__(self) -> bool:
        return self.status != 0

def index(request):
    template = loader.get_template('app/new_questions.html')
    context = {
        "page": Paginator(Question.objects.all(), 10).get_page(request.GET.get("page", 1)),
        "popular_tags": Tag.objects.all()[:10],
        "best_members": Profile.objects.all()[:10]
    }

    context["page_range"] = context["page"].paginator.get_elided_page_range(context["page"].number)

    return HttpResponse(template.render(context, request))

def ask(request):
    template = loader.get_template('app/ask.html')
    context = {
        "popular_tags": Tag.objects.all()[:10],
        "best_members": Profile.objects.all()[:10]
    }
    return HttpResponse(template.render(context, request))

def question(request, question_id):
    template = loader.get_template('app/one_question.html')
    
    context = {
        "question": Question.objects.get_by_id(question_id),
        "answers": Answer.objects.get_by_question_id(question_id),
        "popular_tags": Tag.objects.all()[:10],
        "best_members": Profile.objects.all()[:10]
    }

    return HttpResponse(template.render(context, request))


def tag(request, tag):
    template = loader.get_template('app/tag_questions.html')
    context = {
        "tag": tag,
        "page": Paginator(Question.objects.get_by_tag_name(tag), 10).get_page(request.GET.get("page", 1)),
        "popular_tags": Tag.objects.all()[:10],
        "best_members": Profile.objects.all()[:10]
    }

    context["page_range"] = context["page"].paginator.get_elided_page_range(context["page"].number)

    return HttpResponse(template.render(context, request))

def settings(request):
    template = loader.get_template('app/settings.html')
    context = {
        "popular_tags": Tag.objects.all()[:10],
        "best_members": Profile.objects.all()[:10]
    }
    return HttpResponse(template.render(context, request))

def signin(request):
    template = loader.get_template('app/signin.html')
    context = {
        "error": Error(1, "some wrong data"),
        "popular_tags": Tag.objects.all(),
        "best_members": Profile.objects.all()
    }

    return HttpResponse(template.render(context, request))

def signup(request):
    template = loader.get_template('app/signup.html')
    context = {
        "error": Error(1, "some wrong data"),
        "popular_tags": Tag.objects.all(),
        "best_members": Profile.objects.all()
    }

    return HttpResponse(template.render(context, request))

def hot(request):
    template = loader.get_template('app/hot_questions.html')
    context = {
            "page": Paginator(Question.objects.get_most_by_popularity(100), 10).get_page(request.GET.get("page", 1)),
            "popular_tags": Tag.objects.all()[:10],
            "best_members": Profile.objects.all()[:10]
    }

    context["page_range"] = context["page"].paginator.get_elided_page_range(context["page"].number)

    return HttpResponse(template.render(context, request))

