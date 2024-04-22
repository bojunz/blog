from . import views
from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('index/', views.index),
    path('get_test/', views.get_test,name='get_test'),
    path('get_post/', views.get_post,name='get_post'),
    path('upload/',views.Upload.as_view(),name='upload'),
    path('json/',views.json_test,name='json'),
    path('set_ck/',views.set_ck),
    path('get_ck/',views.get_ck),


]
