from django.contrib import admin
from .models import Reponse, Question, Associer, Image, Tag, Contenir, Concerner

def image(obj):
    return obj.image.image
image.short_description = 'Image'
image.admin_order_field = 'image__cleImage'

def tags_question_count(obj):
        return obj.tags.count()
tags_question_count.short_description = "Tags Count"

class ConcernerAdmin(admin.ModelAdmin):
    list_display = ('question', 'tag', 'id')
    list_filter = ('question', 'tag')

admin.site.register(Concerner, ConcernerAdmin)

class ContenirAdmin(admin.ModelAdmin):
    list_display = (image, 'tag')
    list_filter = ('image', 'tag')
admin.site.register(Contenir, ContenirAdmin)

class ConcernerTabularInline(admin.TabularInline):
    model = Concerner

class ContenirTabularInline(admin.TabularInline):
    model = Contenir

class AssocierTabularInline(admin.TabularInline):
    model = Associer

class ImageAdmin(admin.ModelAdmin):
    list_display = ('titre', 'cleImage')
    list_filter =  ( 'tags',)
    inlines = [ContenirTabularInline,]
admin.site.register(Image, ImageAdmin)

class AssocierAdmin(admin.ModelAdmin):
    list_display = ('question', 'reponse')
    list_filter = ('question', 'reponse')
admin.site.register(Associer, AssocierAdmin)

class ReponseAdmin(admin.ModelAdmin):
    list_display = ('descriptionReponse', 'cleReponse')
admin.site.register(Reponse, ReponseAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('descriptionQuestion', 'cleQuestion', 'priority')
    list_filter =  (('reponses', admin.RelatedOnlyFieldListFilter), ('tags', admin.RelatedOnlyFieldListFilter),)
    inlines = [AssocierTabularInline, ConcernerTabularInline]
admin.site.register(Question, QuestionAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'cleTag')
admin.site.register(Tag, TagAdmin)