from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm


def sign_in(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "users/login.html", {"form": form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(
                    request, f"Hello {username.title()}. Добро пожаловать!"
                )
                return redirect("Posts")

        messages.error(request, "invalid username/password")
        return render(request, "users/login.html", {"form": form})


def sign_out(request):
    logout(request)
    messages.success(request, f"Вы вышли из аккаунта")
    return redirect("login")
