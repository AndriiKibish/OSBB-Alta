# coding: utf-8

from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from .forms import CustomUserCreationForm


def home(request):
    return render(request, 'users/home.html')


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')


class CurrentView(LoginRequiredMixin, TemplateView):
    template_name = 'users/current.html'


class UserLoginView(LoginView):
    template_name = 'users/login.html'  # Шаблон для страницы входа
    redirect_authenticated_user = True  # Если пользователь уже аутентифицирован, перенаправить
    success_url = reverse_lazy('home')  # Куда перенаправить после успешного входа

    def get_success_url(self):
        """Возвращает URL для перенаправления после успешного входа."""
        return self.success_url or super().get_success_url()


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Куда перенаправить после выхода (имя маршрута)


