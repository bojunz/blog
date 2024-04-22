from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index,name='index'),
    path('add/', views.blog_add,name='add'),
    path('list/', views.blog_list,name='list'),
    path('detail/<blog_id>/', views.blog_detail,name='detail'),
    path('delete/<blog_id>/', views.blog_delete,name='delete'),
    path('query/', views.model_info,name='info'),
    path('edit/<blog_id>/', views.blog_update,name='edit'),
    path('cls_update/<blog_id>/', views.Blog_update.as_view(),name='cls_update'),
    path('permission/', views.permission_add,name='per'),
    path('page_test/',views.page_test,name='page_test'),
]