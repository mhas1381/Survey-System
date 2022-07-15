from random import choices
from secrets import choice
from django.shortcuts import render,redirect
from django.contrib.auth import login , logout,authenticate
from polls.models import *
# Create your views here.
def login_page(request):
    return render(request, 'accounts/login.html')
def logged_in(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            questions = Question.objects.all()
            context = {'questions': questions}
            if user is not None:
                login(request, user)
                return render(request,'survey/index.html',context)