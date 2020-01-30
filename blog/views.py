from django.shortcuts import render
from .models import Question, Associer, Tag, Image, Contenir, Concerner
from django.db.models import Count
from .forms import AnswerForm
from django.http import HttpResponseRedirect
#from django.core import serializers

# Create your views here.

def post_list(request):
    return render(request, 'base.html', {})

# Méthode qui retourne la page d'accueil
def accueil(request):
    request.session['tags'] = ""
    request.session['no_tags'] = ""
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
            tag = form.cleaned_data['tag']
            print(tag)
            no_tag = form.cleaned_data['no_tag']
            print(no_tag)
            
            tags = request.session['tags']
            no_tags = request.session['no_tags']
            cletag = 0
            if tag!="":
                cletag =  Tag.objects.all().filter(tag = tag).values_list()[0][0]
                tags = tags + "," + str(cletag)
            else:
                cletag =  Tag.objects.all().filter(tag = no_tag).values_list()[0][0]
                no_tags = no_tags + "," + str(cletag)
            print(cletag)
            print(tags)
            print(no_tags)

            tags = tags.split(",")
            tags.remove('')

            no_tags = no_tags.split(",")
            no_tags.remove('')

            contain = Contenir.objects.all()
            concerns = Concerner.objects.all()
            
            for i in range(len(tags)):
                contain = contain.filter(tag = int(tags[i]))
                concerns = concerns.filter(tag = int(tags[i]))

            for i in range(len(no_tags)):
                contain = contain.exclude(tag = int(no_tags[i]))
                concerns = concerns.exclude(tag = int(no_tags[i]))

            print(contain)
            print(concerns)
            if len(concerns.values_list())!=0:
                clequestion =  concerns.values_list()[0][2]
                question = Question.objects.all().filter( cleQuestion = clequestion)[0]
                print(question)
                associee = Associer.objects.filter(question = clequestion)
                print(question.cleQuestion)
                print(associee)

    else:
        question = Question.objects.get(cleQuestion=1)
        associee = Associer.objects.filter(question = question)
        q = Associer.objects.filter(question = question).count()

    return render(request, 'blog/jouer.html', {'question': question, 'associee': associee})


def after_reponse(request):
    question = Question.objects.get(cleQuestion=1)
    associee = Associer.objects.filter(question = question)

    return render(request, 'blog/liens.html', {'question': question, 'associee': associee,'q': q})
