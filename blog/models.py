from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#Ibrahim
class Joueur(models.Model):
    cleJoueur = models.IntegerField(primary_key = True)
    nomJoueur = models.CharField(max_length = 50)
    passe = models.CharField(max_length = 100)

#Aguibou
class Question(models.Model):
    b = 1

class Image(models.Model):
    cleImage = models.IntegerField().primary_key = True
    image = models.ImageField()
    auteur = models.CharField(max_length=100)
    date_creation = models.DateTimeField(default=timezone.now) 
    designation = models.CharField(max_length=100)
    matiere_technique = models.CharField(max_length=100)
    domaine = models.CharField(max_length=50)
    titre = models.CharField(max_length=200)
    sujet = models.TextField()
    
    joueurs = models.ManyToManyField(Joueur, related_name="images", blank=True)
    questions = models.ManyToManyField(Question, related_name="images", blank=True)
    
    def afficher_image(self):
        # Pas totalement fini, 1ere étape...
        print(self.image)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Avis(models.Model):
    cleAvis = models.IntegerField(primary_key = True)
    aime = models.BooleanField()
    commentaire = models.CharField(max_length = 500)
    cleJoueur = models.ForeignKey(Joueur,on_delete = models.CASCADE)
    cleImage = models.ForeignKey(Image,on_delete = models.CASCADE)