from django.urls import path

from . import views

urlpatterns = [
    path('home', views.diaries, name="home"),
    path('detail', views.book_detail, name="book_detail")
]