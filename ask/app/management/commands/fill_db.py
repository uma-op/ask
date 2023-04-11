from django.core.management.base import BaseCommand
from app.models import Profile, Question, Tag, Answer, AnswerMark, QuestionMark

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("ratio", type=int)

    def handle(self, *args, **options):
        ratio = options["ratio"]

