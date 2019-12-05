from django.contrib import admin
from .models import Post, Reponse, Question, Associer, Image, Joueur, Avis, Tag, Contenir, Concerner

admin.site.register(Post)
admin.site.register(Image)
admin.site.register(Reponse)
admin.site.register(Question)
admin.site.register(Associer)
admin.site.register(Joueur)
admin.site.register(Avis)
admin.site.register(Concerner)
admin.site.register(Tag)
admin.site.register(Contenir)