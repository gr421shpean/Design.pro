from django.urls import path, include
from . import views
from django.urls import re_path as url


urlpatterns = [
    path('', views.base, name='base'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    url('application/', views.ApplicationListView.as_view(), name='application'),
    path('personalarea/', views.personalarea, name='personalarea'),
]