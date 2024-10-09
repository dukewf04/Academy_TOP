from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Question, Choice


# Формы представлений для страниц приложения
class IndexView(generic.ListView):
    model = Question
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("pub_date")[:2]

    # try:
    #     latest_question_list = Question.objects.order_by("-pub_date")[:5]
    #     templeate = loader.get_template("polls/index.html")
    #     context = {
    #         "latest_question_list": latest_question_list,
    #         "request": request,
    #     }
    # except:
    #     raise Http404("Нет вопросов")
    # # output = ", ".join([q.question_text for q in latest_question_list])
    # return HttpResponse(templeate.render(context, request))


# Действие с опросами
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except KeyError:
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "Вы не сделали выбор!",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponse(reverse("polls:results", args=(question.id,)))
