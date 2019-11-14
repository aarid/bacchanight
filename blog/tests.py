import os
from PIL import Image
from django.test import TestCase
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your tests here.

class Test_image(models.Model):

    #Creation d'une methode __init__ qui permet d'acceder à toutes les methodes passer
    #en parametre. Grace à self, on peut cree nos getters (et setters si neccessaire)
    def __init__(self, auteur, date_creation, designation, titre, sujet):
        self._auteur = auteur
        self.__date_creation = date_creation
        self.__designation = designation
        self.__titre = titre
        self.__sujet = sujet

    def get_Auteur(self):
        return self._auteur
    
    def get_Date_creation(self):
        return self.__date_creation

    def get_Designation(self):
        return self.__designation

    def get_Titre(self):
        return self.__titre

    def get_Sujet(self):
        return self.__sujet

    #On recupere les pixels de l'image et fait un teste pour la grandeur
    image = models.ImageField()
    def pixels_images(image):
        hauteur = image.height
        largeur = image.width
        for i in range(hauteur):
            for j in range(largeur):
                c = Image.getpixel(image, (i,j))
        if ((c < 400) or (c > 1800)):
            print("L'image n'est pas de bon qualité")

    taille = os.path.getsize(image)
    #taille = os.path.getsize(Image(models.Model))
    if (taille == 0){
        print("Votre image est vide")
    }
    """Pour la taille de l'image, afin d'avoir des images par assez lourde 
    pour le chargement de la connection (40Ko = 40000 octets)"""
    if (taille < 25000 or taille > 500000):
        print("La taille de l'image est très petite ou très élevée")

    

    
