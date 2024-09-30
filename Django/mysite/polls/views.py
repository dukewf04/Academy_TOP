from django.http import HttpResponse
from django.shortcuts import render


# Формы представлений для страниц приложения
def index(request):
    return HttpResponse("<b>Hello User!</b>")


# Действие с опросами
def detail(request, question_id):
    return HttpResponse("You're looking at question", question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
