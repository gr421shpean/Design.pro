from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]