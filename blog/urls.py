from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='base'),
    path('jouer/', views.jouer, name='play_button'),
    path('rejoue/', views.replay, name='replay'),
    path('contacter/', views.contacter, name='contacter'),
    path('faq/', views.faq, name='faq'),
    path('qui-sommes-nous/', views.qui_sommes_nous, name='qui_sommes_nous'),
    path('not_found/', views.not_found, name='not_found'),
    path('thanks/', views.thanks, name='thanks'),

    path('faq_jouer/', views.faq_jouer, name='faq_jouer'),
    path('Quel-est-le-secret-de-Bacchantor /', views.faq_secret, name='faq_secret'),
    path('Comprendre_nos_algorithmes/', views.faq_algo, name='faq_algo'),
    path('objectif_du_jeu/', views.faq_objectif, name='faq_objectif'),
]
