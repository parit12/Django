from .views import roomView
from django.urls import path

urlpatterns = [
    path('home',roomView.as_view())
]