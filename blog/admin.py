from django.contrib import admin
from django import forms
from .models import Post, Reponse, Question, Associer, Image, Tag, Contenir, Concerner

admin.site.register(Post)

def descriptionQuestion(obj):
    return obj.question.descriptionQuestion
descriptionQuestion.short_description = 'Question'
descriptionQuestion.admin_order_field = 'question_id'

def descriptionReponse(obj):
    return obj.reponse.descriptionReponse
descriptionReponse.short_description = 'Reponse'
descriptionReponse.admin_order_field = 'reponse_id'

def tag(obj):
    return obj.tag.tag
tag.short_description = 'Tag'
tag.admin_order_field = 'cleTag'

def image(obj):
    return obj.image.image
image.short_description = 'Image'
image.admin_order_field = 'cleImage'

class ConcernerAdmin2(admin.ModelAdmin):
    list_display = (descriptionQuestion, tag)
class ConcernerAdmin(admin.TabularInline):
    model = Concerner
admin.site.register(Concerner, ConcernerAdmin2)

class ContenirAdmin2(admin.ModelAdmin):
    list_display = (image, tag)
class ContenirAdmin(admin.TabularInline):
    model = Contenir
admin.site.register(Contenir, ContenirAdmin2)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('titre', 'cleImage')
admin.site.register(Image, ImageAdmin)

class AssocierAdmin2(admin.ModelAdmin):
    list_display = (descriptionQuestion, descriptionReponse)
class AssocierAdmin(admin.TabularInline):
    model = Associer
admin.site.register(Associer, AssocierAdmin2)

class ReponseAdmin(admin.ModelAdmin):
    fields = ('descriptionReponse',)
    list_display = ('descriptionReponse', 'cleReponse')
admin.site.register(Reponse, ReponseAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('descriptionQuestion', 'cleQuestion')
    list_filter =  (('reponses', admin.RelatedOnlyFieldListFilter),)
    model = Question
    inlines = [AssocierAdmin,]
admin.site.register(Question, QuestionAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'cleTag')
    inlines = [ContenirAdmin, ConcernerAdmin,]
admin.site.register(Tag, TagAdmin)