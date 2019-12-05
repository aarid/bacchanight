from django.shortcuts import render
from .models import Question, Associer
from django.db.models import Count

# Create your views here.

def post_list(request):
    return render(request, 'blog/acceuil.html', {})

def jouer(request):
    question = Question.objects.get(cleQuestion=1)
    associee = Associer.objects.filter(question = question)
    #tag = 

    return render(request, 'blog/liens.html', {'question': question, 'associee': associee})


def after_reponse(request):
    question = Question.objects.get(cleQuestion=1)
    associee = Associer.objects.filter(question = question)

    return render(request, 'blog/liens.html', {'question': question, 'associee': associee})
