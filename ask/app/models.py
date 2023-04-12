from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=False
    )

    login = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255)
    popularity = models.BigIntegerField()

class Tag(models.Model):
    name = models.CharField(max_length=255)
    popularity = models.BigIntegerField()

class QuestionManager(models.Manager):
    def get_most_by_popularity(self, quantity):
        return self.order_by("-marks")[:quantity]

    def get_by_tag_name(self, name):
        return self.filter(tags__name=name)

    def get_by_id(self, id):
        return self.get(id=id)


class Question(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    theme = models.CharField(max_length=255)
    text = models.TextField()
    answers = models.BigIntegerField()
    marks = models.BigIntegerField()

    tags = models.ManyToManyField(Tag)

    objects = QuestionManager()

class AnswerManager(models.Manager):
    def get_by_question_id(self, id):
        return self.filter(question__id=id)

class Answer(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )

    text = models.TextField()
    is_correct = models.BooleanField()
    marks = models.BigIntegerField()

    objects = AnswerManager()

class AnswerMark(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    answer = models.ForeignKey(
        Answer,
        on_delete=models.CASCADE
    )

    is_like = models.BooleanField()

class QuestionMark(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )

    is_like = models.BooleanField()

