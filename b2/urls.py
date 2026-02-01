from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('login/verify/otn/vot/', views.voting, name='voting'),
    path('login/verify/', views.send, name='send'),
    path('login/verify/otn/', views.otp, name='otn'),
    path('api/register/', views.api_register, name='api_register'),
]
