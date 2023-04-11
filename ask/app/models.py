from django.db import models

class Profile(models.Model):
    # id =
    user = models.BigIntegerField()  # OneToOne to django user
    login = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255)
    popularity = models.BigIntegerField()

class Tag(models.Model):
    name = models.CharField(max_length=255)
    popularity = models.BigIntegerField()

class Question(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    theme = models.CharField(max_length=255)
    preview_text = models.CharField(max_length=2048)
    text = models.TextField()
    marks = models.BigIntegerField()

    tags = models.ManyToManyField(Tag)

class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )

    text = models.TextField()
    is_correct = models.BooleanField()
    marks = models.BigIntegerField()

class AnswerMark(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    answer = models.ForeignKey(
        Answer,
        on_delete=models.CASCADE
    )

class QuestionMark(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )

