from .views import roomView,CreateRoomView
from django.urls import path

urlpatterns = [
    path('home',roomView.as_view()),
    path('create-room',CreateRoomView.as_view())
]