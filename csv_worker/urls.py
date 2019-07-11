from django.urls import path, include
from . import views

app_name = 'csv_worker'

urlpatterns = [
    path('', views.show, name='home'),
]