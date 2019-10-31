from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Question(models.Model):
    _id = models.AutoField(primary_key=True)
    title = models.CharField(blank = False , max_length=100)
    no_of_answers = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Q_info(models.Model):
    body = models.TextField()
    question = models.OneToOneField(Question ,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    is_anonymous = models.BooleanField(default=True)


class Answer(models.Model):
    _id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class A_info(models.Model):
    answer = models.OneToOneField(Answer , on_delete=models.CASCADE)
    text = models.TextField()
    is_anonymous = models.BooleanField(default=True)
    upvotes = models.IntegerField(default=0)

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer , on_delete=models.CASCADE)

class Upvotes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer , on_delete=models.CASCADE)
