from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse

from .models import Profile, Tag, Question, Answer, QuestionMark, AnswerMark 

from .forms import AnswerForm, AskForm, LoginForm, RegistrationForm

import django.contrib.auth as auth
from django.contrib.auth.decorators import login_required

def index(request):
    context = {
        "page": Paginator(Question.objects.all().order_by('id'), 10).get_page(request.GET.get("page", 1)),
        "popular_tags": Tag.objects.get_most_by_popularity(10),
        "best_members": Profile.objects.all()[:10],
        "user": None if not request.user.is_authenticated else Profile.objects.get_by_user(request.user)
    }

    context["page_range"] = context["page"].paginator.get_elided_page_range(context["page"].number)

    return render(request, "app/new_questions.html", context)

def ask(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/signin?next=/ask")

    if request.method == "POST":
        form = AskForm(request.POST)

        if form.is_valid():
            print("VALID")

            profile = Profile.objects.get_by_user(request.user)

            new_question = Question.objects.create(
                profile=profile,
                theme=form.cleaned_data['theme'],
                text=form.cleaned_data['text'],
                answers=0,
                marks=0
            )

            for tag_name in form.cleaned_data['tags'].split(", "):
                if not tag_name:
                    break

                tag = Tag.objects.get_or_create(name=tag_name)[0]
                tag.popularity += 1
                new_question.tags.add(tag)

                tag.save()

            new_question.save()

            return HttpResponseRedirect(f"/question/{new_question.id}")

    else:
        form = AskForm()

    context = {
        "popular_tags": Tag.objects.get_most_by_popularity(10),
        "best_members": Profile.objects.all()[:10],
        "user": None if not request.user.is_authenticated else Profile.objects.get_by_user(request.user),
        "form": form
    }

    return render(request, "app/ask.html", context)

def question(request, question_id):
    if request.method == "POST":
        form = AnswerForm(request.POST)

        if form.is_valid():
            question = Question.objects.get_by_id(question_id)

            new_answer = Answer(
                profile=Profile.objects.get_by_user(request.user),
                question=question,
                text=form.cleaned_data['text'],
                is_correct=0,
                marks=0
            )

            question.answers += 1

            new_answer.save()
            question.save()

            return HttpResponseRedirect(f"/question/{question_id}")

    else:
        form = AnswerForm()

    context = {
        "question": Question.objects.get_by_id(question_id),
        "answers": Answer.objects.get_by_question_id(question_id),
        "popular_tags": Tag.objects.get_most_by_popularity(10),
        "best_members": Profile.objects.all()[:10],
        "user": None if not request.user.is_authenticated else Profile.objects.get_by_user(request.user),
        "form": form
    }

    return render(request, "app/one_question.html", context)

def tag(request, tag):
    context = {
        "tag": tag,
        "page": Paginator(Question.objects.get_by_tag_name(tag), 10).get_page(request.GET.get("page", 1)),
        "popular_tags": Tag.objects.get_most_by_popularity(10),
        "best_members": Profile.objects.all()[:10],
        "user": None if not request.user.is_authenticated else Profile.objects.get_by_user(request.user)
    }

    context["page_range"] = context["page"].paginator.get_elided_page_range(context["page"].number)

    return render(request, "app/tag_questions.html", context)

def settings(request):
    context = {
        "popular_tags": Tag.objects.get_most_by_popularity(10),
        "best_members": Profile.objects.all()[:10],
        "user": None if not request.user.is_authenticated else Profile.objects.get_by_user(request.user)
    }

    return render(request, "app/settings.html", context)

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            user = auth.authenticate(request, username=form.cleaned_data['login'], password=form.cleaned_data['password'])
            
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect(request.GET.get("next") if request.GET.get("next") is not None else "/")

            form.add_error(field=None, error="Incorrect login or password")

    else:
        form = LoginForm()

    context = {
        "popular_tags": Tag.objects.get_most_by_popularity(10),
        "best_members": Profile.objects.all()[:10],
        "form": form,
        "user": None if not request.user.is_authenticated else Profile.objects.get_by_user(request.user),
    }

    return render(request, "app/signin.html", context)

def signup(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['repeat_password']:
                user = User.objects.create_user(username=form.cleaned_data['login'], password=form.cleaned_data['password'])
                profile = Profile(
                    user=user,
                    login=request.POST['login'],
                    email=request.POST['email'],
                    nickname=request.POST['nickname'],
                    popularity=0
                )

                profile.save()

                return HttpResponseRedirect("/")

            form.add_error(field=None, error="Password mismatch")

    else:
        form = RegistrationForm()

    context = {
        "popular_tags": Tag.objects.get_most_by_popularity(10),
        "best_members": Profile.objects.all()[:10],
        "form" : form,
        "user": None if not request.user.is_authenticated else Profile.objects.get_by_user(request.user)
    }

    return render(request, "app/signup.html", context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

def hot(request):
    context = {
        "page": Paginator(Question.objects.get_most_by_popularity(100), 10).get_page(request.GET.get("page", 1)),
        "popular_tags": Tag.objects.get_most_by_popularity(10),
        "best_members": Profile.objects.all()[:10],
        "user": None if not request.user.is_authenticated else Profile.objects.get_by_user(request.user)
    }

    context["page_range"] = context["page"].paginator.get_elided_page_range(context["page"].number)

    return render(request, "app/hot_questions.html", context)

