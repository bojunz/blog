from django.contrib import admin
from django.urls import path ,include
from . import views
urlpatterns = [
    path('home/', views.home,name='home'),
    path('login/', views.LoginTest.as_view(),name='login'),
    path('logout/', views.logout_test,name='logout'),
    path('register/', views.RegisterTest.as_view(),name='register'),
    path('login1/', views.Login.as_view(),name='login1'),
]
