from django.shortcuts import render
from .models import Question

# Create your views here.

def post_list(request):
    return render(request, 'blog/acceuil.html', {})

def jouer(request):
    return render(request, 'blog/liens.html', {})
