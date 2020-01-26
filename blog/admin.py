from django.contrib import admin
from .models import Post, Reponse, Question, Associer, Image, Joueur, Avis, Tag, Contenir, Concerner

admin.site.register(Post)

class ConcernerAdmin(admin.TabularInline):
    model = Concerner
admin.site.register(Concerner)
class ContenirAdmin(admin.TabularInline):
    model = Contenir
admin.site.register(Contenir)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'cleImage')
admin.site.register(Image, ImageAdmin)
class AssocierAdmin(admin.TabularInline):
    model = Associer
admin.site.register(Associer)
class ReponseAdmin(admin.ModelAdmin):
    list_display = ('descriptionReponse', 'cleReponse')
admin.site.register(Reponse, ReponseAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('descriptionQuestion', 'cleQuestion')
    model = Question
    inlines = [AssocierAdmin,]
admin.site.register(Question, QuestionAdmin)

admin.site.register(Joueur)
class AvisAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
admin.site.register(Avis)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'cleTag')
    inlines = [ContenirAdmin, ConcernerAdmin,]
admin.site.register(Tag, TagAdmin)