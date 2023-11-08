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
    path('main_request/', views.ApplicationCreate.as_view(), name='main_request'),
    path('my_request/', views.MyPostListViews.as_view(), name='my_request'),
    path('request/<int:pk>/delete/', views.ApplicationDelete.as_view(), name='application_confirm_delete'),
    path('admin_base/', views.ApplicationListViewAdmin.as_view(), name='admin_base'),
]