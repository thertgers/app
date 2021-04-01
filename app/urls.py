"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.conf.urls import url
from notes import views

urlpatterns = [
    url(r'^password/$', views.change_password, name='change_password'),
    path('register/', views.register, name='register'),
    path('accounts/login/', views.Userlogin, name='login'),
    path('accounts/login/', views.Userlogin, name='logout'),

    path('',views.home, name=''),
    path('home/',views.home, name='home'),

    path('category/list', views.category_list, name='category/list'),
    path('category/add', views.category_add, name='category/add'),
    path('category/get/<int:id>', views.category_get, name='category/get'),
    path('category/delete/<int:id>', views.category_delete, name='category/delete'),
    path('category/update/<int:id>', views.category_update, name='category/update'),

    path('project/list', views.project_list, name='project/list'),
    path('project/add', views.project_add, name='project/add'),
    path('project/get/<int:id>', views.project_get, name='project/get'),
    path('project/delete/<int:id>', views.project_delete, name='project/delete'),

    path('note/add', views.note_add, name='note/add'),
    path('note/update/<int:id>', views.note_update, name='note/update'),
    path('note/delete/<int:id>', views.note_delete, name='note/delete'),
    path('note/<int:id>/upload/', views.note_upload, name='note/upload')
]
