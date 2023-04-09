from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator

class Question:
    def __init__(self, id, theme, text, ans_count, tags, avatar, mark) -> None:
        self.id = id
        self.theme = theme
        self.preview_text = text
        self.text = text
        self.ans_count = ans_count
        self.tags = tags
        self.avatar = avatar
        self.mark =  mark

class Answer:
    def __init__(self, text, mark, is_correct, avatar) -> None:
        self.text = text
        self.mark = mark
        self.is_correct = is_correct
        self.avatar = avatar

class Error:
    def __init__(self, status, details="") -> None:
        self.status = status
        self.details = details

    def __bool__(self) -> bool:
        return self.status != 0

questions = [
    Question(
        0,
        "theme1",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        1,
        ["tag1"],
        "img/ava.png",
        1,
    ),
    Question(
        1,
        "theme1",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        1,
        ["tag1"],
        "img/ava.png",
        1,
    ),
    Question(
        2,
        "theme2",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        2,
        ["tag1", "tag2"],
        "img/ava.png",
        2,
        ),
    Question(
        3,
        "theme3",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        3,
        ["tag3"],
        "img/ava.png",
        4,
    ),
    Question(
        4,
        "theme4",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        4,
        [],
        "img/ava.png",
        8,
    ),
    Question(
        5,
        "theme5",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        5,
        ["tag_hueg"],
        "img/ava.png",
        16,
    ), 
    Question(
        6,
        "theme5",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        5,
        ["tag_hueg"],
        "img/ava.png",
        16,
    ),
    Question(
        7,
        "theme5",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        5,
        ["tag_hueg"],
        "img/ava.png",
        16,
    ), 
    Question(
        8,
        "theme5",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        5,
        ["tag_hueg"],
        "img/ava.png",
        16,
    ),
    Question(
        9,
        "theme5",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        5,
        ["tag_hueg"],
        "img/ava.png",
        16,
    ), 
    Question(
        10,
        "theme5",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        5,
        ["tag_hueg"],
        "img/ava.png",
        16,
    ),
    Question(
        11,
        "theme5",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        5,
        ["tag_hueg"],
        "img/ava.png",
        16,
    ), 
    Question(
        12,
        "theme5",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        5,
        ["tag_hueg"],
        "img/ava.png",
        16,
    )
]

answers = [
    Answer(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        1,
        True,
        "img/ava.png"
    ),
    Answer(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        2,
        False,
        "img/ava.png"
    ),
    Answer(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        3,
        True,
        "img/ava.png"
    ),
    Answer(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        4,
        False,
        "img/ava.png"
    ),
    Answer(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        5,
        False,
        "img/ava.png"
    )
]

tags = [
    "tag1",
    "tag2",
    "tag3",
    "tag4"
]

members = [
    "best member 1",
    "best member 2",
    "best member 3"
]


def index(request):
    template = loader.get_template('app/new_questions.html')
    context = {
        "page": Paginator(questions, 1).get_page(request.GET.get("page", 1)),
        "popular_tags": tags,
        "best_members": members
    }

    context["page_range"] = context["page"].paginator.get_elided_page_range(context["page"].number)

    return HttpResponse(template.render(context, request))

def ask(request):
    template = loader.get_template('app/ask.html')
    context = {
        "popular_tags": tags,
        "best_members": members
    }
    return HttpResponse(template.render(context, request))

def question(request, question_id):
    template = loader.get_template('app/one_question.html')
    context = {
        "question": questions[question_id],
        "answers": answers,
        "popular_tags": tags,
        "best_members": members
    }

    return HttpResponse(template.render(context, request))


def tag(request, tag):
    template = loader.get_template('app/tag_questions.html')
    context = {
        "tag": tag,
        "page": Paginator(questions, 1).get_page(request.GET.get("page", 1)),
        "popular_tags": tags,
        "best_members": members
    }

    context["page_range"] = context["page"].paginator.get_elided_page_range(context["page"].number)

    return HttpResponse(template.render(context, request))

def settings(request):
    template = loader.get_template('app/settings.html')
    context = {
        "popular_tags": tags,
        "best_members": members
    }
    return HttpResponse(template.render(context, request))

def signin(request):
    template = loader.get_template('app/signin.html')
    context = {
        "error": Error(1, "some wrong data"),
        "popular_tags": tags,
        "best_members": members
    }

    return HttpResponse(template.render(context, request))

def signup(request):
    template = loader.get_template('app/signup.html')
    context = {
        "error": Error(1, "some wrong data"),
        "popular_tags": tags,
        "best_members": members
    }

    return HttpResponse(template.render(context, request))

def hot(request):
    template = loader.get_template('app/hot_questions.html')
    context = {
            "page": Paginator(questions, 1).get_page(request.GET.get("page", 1)),
            "popular_tags": tags,
            "best_members": members
    }

    context["page_range"] = context["page"].paginator.get_elided_page_range(context["page"].number)

    return HttpResponse(template.render(context, request))

