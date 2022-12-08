from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .forms import UserRegisterForm


class UserRegisterView(View):
    def get(self, request, *args, **kwargs):
        form = UserRegisterForm
        return render(request, "register.html", {"form": form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f"Вы успешно зарегистрировались! Можете авторизоваться!")
            return redirect("login")
        else:
            form = UserRegisterForm()
        return render(request, "register.html", {"form": form})
