from django.conf import settings
from django.db import models
from django.utils import timezone

# effacer manuellement la liste des requêtes
from django.db import reset_queries
reset_queries()

class Reponse(models.Model):
    cleReponse = models.IntegerField(primary_key=True)
    descriptionReponse = models.CharField(max_length= 200)

    def __str__(self):
        return self.descriptionReponse

class Tag(models.Model):
    cleTag = models.IntegerField(primary_key = True)
    tag = models.CharField(max_length=200)

    def __str__(self):
        return self.tag

class Question(models.Model):
    cleQuestion = models.IntegerField(primary_key = True)
    descriptionQuestion = models.CharField(max_length=200)
    inclu = models.IntegerField()
    priority = models.IntegerField(default=0)

    reponses = models.ManyToManyField(Reponse, through='Associer')
    tags = models.ManyToManyField(Tag, through='Concerner')
    
    def __str__(self):
        return self.descriptionQuestion

class Associer(models.Model):
    reponse = models.ForeignKey(Reponse, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    tag = models.CharField(max_length=80, blank=True)
    no_tag = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return self.reponse.descriptionReponse + " -- " + self.question.descriptionQuestion

class Image(models.Model):
    cleImage = models.IntegerField(primary_key = True)
    # FileFiel au lieu de image
    image = models.ImageField( null=True)
    auteur = models.CharField(max_length=100)
    date_creation = models.CharField(max_length=20)
    titre = models.CharField(max_length=100)
    matiere_technique = models.CharField(max_length=100)
    domaine = models.CharField(max_length=50)
    sujet = models.TextField()
    lien_musba = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag, through='Contenir')
    
    def __str__(self):
        return self.titre

#la table tag

class Concerner(models.Model):
    tag = models.ForeignKey(Tag, on_delete = models.CASCADE)
    question = models.ForeignKey(Question, on_delete = models.CASCADE) 

    def __str__(self):
        return self.tag.tag + " -- " + self.question.descriptionQuestion

#la table de liaison image tag
class Contenir(models.Model):
    image = models.ForeignKey(Image, on_delete = models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete = models.CASCADE)

    def __str__(self):
        return self.tag.tag + " -- " + self.image.titre
