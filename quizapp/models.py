from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Course(models.Model):
    course_name = models.CharField(max_length=50)
    no_of_questions = models.PositiveIntegerField()
    total_marks = models.PositiveIntegerField()

    def __str__(self):
        return self.course_name


class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    question = models.CharField(max_length=100)

    def __str__(self):
        return self.question


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.option


class UserAttemptHistory(models.Model):
    User_Details = models.ForeignKey(User, on_delete=models.CASCADE)
    Questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    Answer_Given = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
