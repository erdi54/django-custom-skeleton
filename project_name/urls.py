"""{{ project_name }} URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
# Django imports
from django.urls import path, include, re_path
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [

    # provide the most basic login/logout functionality
    path('login/$', auth_views.LoginView.as_view(template_name='core/login.html'),
         name='core_login'),
    path('logout/$', auth_views.LogoutView.as_view(), name='core_logout'),

    # enable the admin interface
    path('admin/', admin.site.urls),
]
