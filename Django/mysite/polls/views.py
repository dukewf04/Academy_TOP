from django.http import HttpResponse
from django.shortcuts import render


# Формы представлений для страниц приложения
def index(request):
    return HttpResponse("<b>Hello User!</b>")
