from django.shortcuts import render
from  polls.models import *
# Create your views here.


def index(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'survey/index.html',context)


def vote(request):
    return render(request, 'vote.html')


def result(request):
    return render(request, 'result.html')
