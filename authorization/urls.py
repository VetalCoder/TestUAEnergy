from django.urls import path, include
from . import views

app_name = 'authorization'

urlpatterns = [
    path('', views.Login.as_view(), name='home'),
]