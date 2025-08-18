# core/urls.py
from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
      path('', home, name='home'),
]
