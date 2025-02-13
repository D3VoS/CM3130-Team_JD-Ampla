"""ampla URL Configuration

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
from django.urls import path, include
from . import views
app_name = "Core"
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('accounts/', include('Accounts.urls', namespace='Accounts')),
    path('calendar/', include('Calendar.urls', namespace='Calendar')),
    path('store/', include('Store.urls', namespace='Store')),
    path('admin/', views.admin_index, name='admin'),
    path('admin/<int:id>', views.findByID, name='findByID'),
    path('admin/archive/<int:id>', views.archive, name='archive'),
    path('admin/archived_forms', views.archived_forms, name='archived_forms'),
]
