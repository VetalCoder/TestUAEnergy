from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserEnergyForm

# Create your views here.


class Login(LoginView):
    template_name = "auth/login.html"
    authentication_form = UserEnergyForm


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('authorization:login')
    template_name = 'auth/signup.html'


class LogOut(LogoutView):
    template_name = 'auth/logged_out.html'
