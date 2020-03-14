"""EZproject001 URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.views import static
from django.urls import re_path
from EZproject001 import settings
from EZsite001 import views

# admin.autodiscover()
# name:SA, code:SA
# path() is not regex
urlpatterns = [
    path("pythonspec/", views.pythonspec),
    path('resume/en/', views.resume_en),
    path('resume/cn/', views.resume_cn),
    path('admin/', admin.site.urls),
    path("webdev/", views.webDev),
    path('course/', views.course),
    path("submit/", views.submit),
    path("pfas/", views.pfas),
    path("pkb/", views.pkb),
    path('', views.index),
]

if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}),
    ]
