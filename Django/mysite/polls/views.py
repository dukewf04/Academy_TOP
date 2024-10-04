from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader

from .models import Question


# Формы представлений для страниц приложения
def index(request):
    try:
        latest_question_list = Question.objects.order_by("-pub_date")[:5]
        templeate = loader.get_template('polls/index.html')
        context = {
            "latest_question_list": latest_question_list,
            "request": request,
        }
    except:
        raise Http404("Нет вопросов")
    #output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(templeate.render(context, request))


# Действие с опросами
def detail(request, question_id):
    return HttpResponse("You're looking at question", question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
