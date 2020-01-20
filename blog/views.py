from django.shortcuts import render
from .models import Question, Associer, Tag, Image, Contenir, Concerner
from django.db.models import Count
from .forms import AnswerForm
from django.http import HttpResponseRedirect

# Create your views here.

def post_list(request):
    #print( request.POST["bidule"] )
    contain = Contenir.objects.all()
    next_questions = Concerner.objects.all()
    #print(contain)
    #print(next_questions)
    return render(request, 'blog/acceuil.html', {'contain': contain, 'next_questions': next_questions})

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
            
            contain = form.cleaned_data['contain']
            print(contain)
            next_questions = form.cleaned_data['next_questions']
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
