from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .forms import RegisterForm
from django.core.paginator import Paginator, EmptyPage
from .models import Question, Course, Choice
# Create your views here.


class IndexView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['total_course'] = Course.objects.all()
        return context


def question_view(request, course_id, question_id):

    question = Question.objects.filter(course=course_id)
    choices = Choice.objects.filter(question=question_id)
    print(question)
    print(choices)
    p = Paginator(question, 1)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    context = {'question': page,
               'choices': choices,
               }

    return render(request, 'quiz.html', context)


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect('/')
    else:
        form = RegisterForm()
    return render(response, "registration/register.html", {'form': form})
