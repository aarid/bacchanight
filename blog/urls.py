from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('jouer/', views.jouer, name='play_button'),
    path('jouer/after_reponse/', views.jouer, name='play_button'),
]