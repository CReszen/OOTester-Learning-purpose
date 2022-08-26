from django.shortcuts import render
from . import models
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def showMenu(request):
    question = models.Question.objects.all()
    return render(request,'task/menu.html',{
    'question':question,
    })

def showQuestion(request, question_id):
    question = models.Question.objects.get(pk=question_id)
    return render(request,'task/question.html',{
        'question':question,
    })

def changeValue(request, id):
    question = models.Question.objects.get(pk=id)
    question.is_complete = True
    question.save()
    return HttpResponseRedirect(reverse('task:menu'))

def getUser(request):
    users =  models.UserDB.objects.all()
    if request.method == "POST":
        form = models.User(request.POST)
        if(form.is_valid()):
            for user in users:
                if user.name == form.name and user.age == form.age:
                    return HttpResponseRedirect(reverse('task:menu'))
    else:
        form = models.User()
    return render(request,'task/user.html',{
        'form':form
    })

def resetQuestion(request):
    question = models.Question.objects.all()
    if request.method == "POST":
        for quest in question :
            quest.is_complete = False
            quest.save();
    return HttpResponseRedirect(reverse('task:menu'))
