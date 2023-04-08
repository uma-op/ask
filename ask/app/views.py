from django.http import HttpResponse
from django.template import loader

class Question:
    def __init__(self, theme, text, ans_count, tags, avatar, mark) -> None:
        self.theme = theme
        self.preview_text = text
        self.text = text
        self.ans_count = ans_count
        self.tags = tags
        self.avatar = avatar
        self.mark =  mark

def index(request):
    template = loader.get_template('app/new_questions.html')
    context = {
        "questions": [ 
            Question(
                "theme1",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                1,
                ["tag1"],
                "img/ava.png",
                1,
            ),
            Question(
                "theme2",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                2,
                ["tag1", "tag2"],
                "img/ava.png",
                2,
            ),
            Question(
                "theme3",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                3,
                ["tag3"],
                "img/ava.png",
                4,
            ),
            Question(
                "theme4",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                4,
                [],
                "img/ava.png",
                8,
            ),
            Question(
                "theme5",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                5,
                ["tag_hueg"],
                "img/ava.png",
                16,
            )
        ],
        "popular_tags": [
            "tag1",
            "tag2",
            "tag3",
            "tag4"
        ],
        "best_members": [
            "best member 1",
            "best member 2",
            "best member 3"
        ]
    }

    return HttpResponse(template.render(context, request))

def ask(request):
    template = loader.get_template('app/ask.html')
    context = dict()
    return HttpResponse(template.render(context, request))

def settings(request):
    template = loader.get_template('app/settings.html')
    context = dict()
    return HttpResponse(template.render(context, request))

def signin(request):
    template = loader.get_template('app/signin.html')
    context = dict()
    return HttpResponse(template.render(context, request))

def signup(request):
    template = loader.get_template('app/signup.html')
    context = dict()
    return HttpResponse(template.render(context, request))

