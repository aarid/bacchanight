from django.shortcuts import render
from .models import Question, Associer, Tag, Image, Contenir, Concerner
from django.db.models import Count
from .forms import AnswerForm
from django.http import HttpResponseRedirect
from django.core import serializers

# Create your views here.

def post_list(request):
    return render(request, 'base.html', {})

# Méthode qui retourne la page d'accueil
def accueil(request):
    request.session['contain'] = serializers.serialize("xml", Contenir.objects.all())
    request.session['next_questions'] = serializers.serialize("xml", Concerner.objects.all())
    return render(request, 'blog/acceuil.html')

# Méthode qui retourne la page Nous contacter
def contacter(request):
    return render(request, 'blog/contacter.html', {})

# Méthode qui retourne la page faq
def faq(request):
    return render(request, 'blog/faq.html', {})

# Méthode qui retourne la page faq
def qui_sommes_nous(request):
    return render(request, 'blog/qui_sommes_nous.html', {})

# Méthode qui retourne la page jouer
def jouer(request):
    question = None
    associee = None
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AnswerForm(request.POST)
        # check whether it's valid:
        print(form)
        if form.is_valid():
            reponse = form.cleaned_data['reponse']
            print(reponse)
            
            contain = serializers.deserialize("xml", request.session['contain'])
            contain
            print(contain)
            next_questions = serializers.deserialize("xml", request.session['next_questions'])
            print(next_questions)
            
            tag = Tag.objects.filter(tag = reponse)
            
            contain = contain.filter(tag = tag)
            
            next_questions = next_questions.filter(tag = tag)

            question =  next_questions[0]
            associee = Associer.objects.filter(question = question)
    else:
        form = AnswerForm()
        question = Question.objects.get(cleQuestion=1)
        associee = Associer.objects.filter(question = question)
        #q = Associer.objects.annotate(number_of_entries = Count('question'))
        q = Associer.objects.filter(question = question).count()

    return render(request, 'blog/jouer.html', {'question': question, 'associee': associee})


def after_reponse(request):
    question = Question.objects.get(cleQuestion=1)
    associee = Associer.objects.filter(question = question)

    return render(request, 'blog/liens.html', {'question': question, 'associee': associee,'q': q})
