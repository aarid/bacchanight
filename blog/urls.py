from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='base'),
    path('jouer/', views.jouer, name='play_button'),
    path('rejouer/', views.replay, name='replay'),
    path('faq/', views.faq, name='faq'),
    path('qui-sommes-nous/', views.qui_sommes_nous, name='qui_sommes_nous'),
    path('not_found/', views.not_found, name='not_found'),
]
