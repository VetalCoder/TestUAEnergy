from django.urls import path
from . import views

app_name = 'authorization'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.Login.as_view(), name='login'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
