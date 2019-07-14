from django.urls import path
from . import views

app_name = 'csv_worker'

urlpatterns = [
    path('', views.CSVLoadView.as_view(), name='home'),
    path('view/', views.ShowTablesView.as_view(), name='view_csv'),
]
