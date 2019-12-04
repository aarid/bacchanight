from django.shortcuts import render
from .models import Question, Associer

# Create your views here.

def post_list(request):
    return render(request, 'blog/acceuil.html', {})

def jouer(request):
    question = Question.objects.get(cleQuestion=1)
    associee = Associer.objects.get(question = question)

    return render(request, 'blog/liens.html', {'question': question, 'associee': associee})
