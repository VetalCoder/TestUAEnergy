from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from .forms import UserEnergyForm

# Create your views here.


class HomeView(TemplateView):
    template_name = 'base.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('csv_worker:home')
        return super().dispatch(request, *args, **kwargs)


class Login(LoginView):
    template_name = "auth/login.html"
    authentication_form = UserEnergyForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('csv_worker:home')
        return super().dispatch(request, *args, **kwargs)


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('authorization:login')
    template_name = 'auth/signup.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('csv_worker:home')
        return super().dispatch(request, *args, **kwargs)


class LogOut(LogoutView):
    pass
