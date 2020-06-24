from django.urls import path

from . import views

urlpatterns = [
    path('start_game', views.start_game, name="start"),
]