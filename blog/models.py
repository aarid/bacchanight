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

class Reponse(models.Model):
    cleReponse = models.IntegerField(primary_key=True)
    descriptionReponse = models.CharField(max_length= 200)

#     def __str__(self):
#         return self.description

class Question(models.Model):
    cleQuestion = models.IntegerField(primary_key = True)
    descriptionQuestion = models.CharField(max_length=200)
    typeQuestion = models.CharField(max_length=200)

    reponses = models.ManyToManyField(Reponse, through='Associer')
    
#     #reponses = models.ManyToManyField(Reponse)

#     def __str__(self):
#         return self.description
class Associer(models.Model):
    reponse = models.ForeignKey(Reponse, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    tag = models.CharField(max_length=80, blank=True)
    no_tag = models.CharField(max_length=80, blank=True)

class Image(models.Model):
    cleImage = models.IntegerField(primary_key = True)
    # FileFiel au lieu de image
    image = models.ImageField( null=True)
    auteur = models.CharField(max_length=100)
    date_creation = models.CharField(max_length=20)
    designation = models.CharField(max_length=100)
    matiere_technique = models.CharField(max_length=100)
    domaine = models.CharField(max_length=50)
    titre = models.CharField(max_length=200)
    sujet = models.TextField()
    
#     def afficher_image(self):
#         # Pas totalement fini, 1ere étape...
#         print(self.image)

#la table tag
class Tag(models.Model):
    cleTag = models.IntegerField(primary_key = True)
    tag = models.CharField(max_length=200)

    image = models.ManyToManyField(Image, through='Contenir')
    questions = models.ManyToManyField(Question, through='Concerner')

class Concerner(models.Model):
    tag = models.ForeignKey(Tag, on_delete = models.CASCADE)
    question = models.ForeignKey(Question, on_delete = models.CASCADE) 


#la table de liaison image tag
class Contenir(models.Model):
    image = models.ForeignKey(Image, on_delete = models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete = models.CASCADE)
