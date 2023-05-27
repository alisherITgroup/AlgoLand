from django.db import models
from django.contrib.auth.models import User

def template():
    return {" ": "Hello World"}

class Problem(models.Model):
    name = models.CharField(max_length=100)
    problem = models.TextField()
    timelimit = models.IntegerField(default=1000)
    memorylimit = models.IntegerField(default=16)
    difficulty = models.IntegerField(default=10)
    comment = models.TextField()
    infoin = models.TextField()
    infoout = models.TextField()
    simpletests = models.JSONField(default=template)
    tests = models.JSONField(default=template)
    solvers = models.ManyToManyField(User, related_name='problem_solvers')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Lesson(models.Model):
    name = models.CharField(max_length=1000)
    video = models.URLField()
    body = models.TextField()
    problems = models.ManyToManyField(Problem, related_name='lesson_problems')
    viewers = models.ManyToManyField(User, related_name='lesson_viewers')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

