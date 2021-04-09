from django.contrib import admin
from .models import Course, Question, UserAttemptHistory, Choice
# Register your models here.


class QuestionInline(admin.TabularInline):
    model = Question


class ChoiceInline(admin.TabularInline):
    model = Choice


class CourseInLine(admin.TabularInline):
    model = Course


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline, ]


class AnswerAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserAttemptHistory)
admin.site.register(Course)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
