from django.conf import settings
from django.db import models
from django.utils import timezone

# effacer manuellement la liste des requêtes
from django.db import reset_queries
reset_queries()

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

# #Ibrahim
class Joueur(models.Model):
    cleJoueur= models.IntegerField(primary_key = True)
    nomJoueur = models.CharField(max_length= 50, null=True)
    motDePasse = models.CharField(max_length=50, null=True)


#Aguibou
class Reponse(models.Model):
    cleReponse = models.IntegerField(primary_key=True)
    descriptionReponse = models.CharField(max_length= 200)

#     def __str__(self):
#         return self.description

class Question(models.Model):
    cleQuestion = models.IntegerField(primary_key = True)
    descriptionQuestion = models.CharField(max_length=200)

    reponses = models.ManyToManyField(Reponse, through='Associer')
    
#     #reponses = models.ManyToManyField(Reponse)

#     def __str__(self):
#         return self.description
class Associer(models.Model):
    reponse = models.ForeignKey(Reponse, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class Image(models.Model):
    cleImage = models.IntegerField(primary_key = True)
    image = models.ImageField()
    auteur = models.CharField(max_length=100)
    date_creation = models.DateTimeField(default=timezone.now) 
    designation = models.CharField(max_length=100)
    matiere_technique = models.CharField(max_length=100)
    domaine = models.CharField(max_length=50)
    titre = models.CharField(max_length=200)
    sujet = models.TextField()
    
    questions = models.ManyToManyField(Question, through='Concerner')
    
#     def afficher_image(self):
#         # Pas totalement fini, 1ere étape...
#         print(self.image)
        
class Concerner(models.Model):
    image = models.ForeignKey(Image, on_delete = models.CASCADE)
    question = models.ForeignKey(Question, on_delete = models.CASCADE) 

class Avis(models.Model):
    cleAvis = models.IntegerField(primary_key = True)
    aime = models.BooleanField(default=False)
    commentaire = models.CharField(max_length = 500, null=True)
    cleJoueur = models.ForeignKey(Joueur,on_delete = models.CASCADE)
    cleImage = models.ForeignKey(Image,on_delete = models.CASCADE)
