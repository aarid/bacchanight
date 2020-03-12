from django.shortcuts import render
from .models import Question, Associer, Tag, Image, Contenir, Concerner
from django.db.models import Count
from .forms import AnswerForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .forms import ContacterNous
#from django.core import serializers

# Create your views here.

def post_list(request):
    return render(request, 'base.html', {})

# Méthode qui retourne la page d'accueil
def accueil(request):
    request.session['tags'] = ""
    request.session['no_tags'] = ""
    request.session['questions_asked'] = ""
    return render(request, 'blog/acceuil.html')

# Méthode qui retourne la page Nous contacter
def contacter(request):
    if request.method == 'POST':
        form = ContacterNous(request.POST)

        if form.is_valid():
            nomPrenon  = form.cleaned_data['nomPrenon']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            mail_admin = ['bahousmane4567@gmail.com']

            send_mail(nomPrenon, subject, message, mail_admin)

            return render(request, 'blog/contacter.html', {'message' : message})
            #return HttpResponseRedirect('/thanks/')

    else:
        form = ContacterNous()

    return render(request, 'blog/contacter.html', {'form': form})


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
            print( "tag = " + tag)
            no_tag = form.cleaned_data['no_tag']
            print(no_tag)

            question_asked = form.cleaned_data['question_asked']
            print("questions_asked = " + question_asked)

            question_asked = form.cleaned_data['question_asked']
            
            tags = request.session['tags']
            no_tags = request.session['no_tags']
            questions_asked = request.session['questions_asked']
            cletag = 0
            if tag!="":
                cletag =  Tag.objects.all().filter(tag = tag).values_list()[0][0]
                tags = tags + "," + str(cletag)
            else:
                if no_tag!="":
                    cletag =  Tag.objects.all().filter(tag = no_tag).values_list()[0][0]
                    no_tags = no_tags + "," + str(cletag)
            print(cletag)
            print("tags = " + tags)
            print(no_tags)
            print(questions_asked)

            if question_asked!="":
                questions_asked = questions_asked + "," +  question_asked

            request.session['tags'] = tags
            request.session['no_tags'] = no_tags
            request.session['questions_asked'] = questions_asked

            tags = tags.split(",")
            tags.remove('')

            no_tags = no_tags.split(",")
            no_tags.remove('')

            questions_asked = questions_asked.split(",")
            questions_asked.remove('')

            contain = Contenir.objects.all()
            concerns = Concerner.objects.all()
            print("Début for")
            print(concerns)
            for i in range(len(tags)):
                print("------------------------------------------------------")
                contain = contain.filter(image__tags = int(tags[i]))
                concerns = concerns.filter(question__tags = int(tags[i]))
                print(concerns)
                

            for i in range(len(no_tags)):
                contain = contain.exclude(image__tags = int(no_tags[i]))
                concerns = concerns.exclude(tag = int(no_tags[i]))
                concerns = concerns.exclude(question__inclu = int(no_tags[i]))

            print("Avant")
            

            for i in range(len(questions_asked)):
                concerns = concerns.exclude(question__cleQuestion = int(questions_asked[i]))

            print(contain)
            print(concerns)
            size_contain = len(contain.values('image').annotate(dcount=Count('image')) )
            print("******************************************")
            print(size_contain)
            size_concerns = concerns.count()

            if size_contain ==1:
                img = contain[0].image
                return render(request, 'blog/afficher_image.html', {'img': img})

            if size_concerns!=0: 
                question = concerns[0].question
                if question.cleQuestion == question_asked and size_concerns>1:
                    question = concerns[1].question
                print(question)
                associee = Associer.objects.filter(question = question.cleQuestion)
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
