"""{{ project_name }} URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
# Django imports
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="{{ project_name }} API",
        default_version='v1',
        description="Welcome to {{ project_name }} Document",
        terms_of_service="erdi.ozcan@outlook.com",
        contact=openapi.Contact(email="erdi.ozcan@outlook.com"),
        license=openapi.License(name="{{ project_name }}"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [  # provide the most basic login/logout functionality
                  path('login/$', auth_views.LoginView.as_view(template_name='core/login.html'),
                       name='core_login'),
                  path('logout/$', auth_views.LogoutView.as_view(), name='core_logout'),
                  # enable the admin interface
                  path('admin/', admin.site.urls),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # noqa E501
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
