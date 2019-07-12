from django.urls import path, include
from . import views
from django.http import HttpResponse

app_name = 'csv_worker'

urlpatterns = [
    path('', views.CSVLoadView.as_view(), name='home'),
    path('view/', HttpResponse, name='view_csv'),
]