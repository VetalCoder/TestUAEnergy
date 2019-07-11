from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Create your views here.


class Login(LoginView):
    template_name = "auth/login.html"
    redirect_field_name = reverse_lazy('csv_worker:home')
