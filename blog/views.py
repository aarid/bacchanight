from django.shortcuts import render
from .models import Question, Associer
from django.db.models import Count
from .forms import AnswerForm
from django.http import HttpResponseRedirect

# Create your views here.

def post_list(request):
    #print( request.POST["bidule"] )
    return render(request, 'blog/acceuil.html', {})

def jouer(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AnswerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            bidule = form.cleaned_data['bidule']
            print(bidule)

    else : 
        form = AnswerForm()
    question = Question.objects.get(cleQuestion=1)
    associee = Associer.objects.filter(question = question)
 #   q = Associer.objects.annotate(number_of_entries = Count('question'))
    q = Associer.objects.filter(question = question).count()
    #tag = 

    return render(request, 'blog/liens.html', {'question': question, 'associee': associee})


def after_reponse(request):
    question = Question.objects.get(cleQuestion=1)
    associee = Associer.objects.filter(question = question)

    return render(request, 'blog/liens.html', {'question': question, 'associee': associee,'q': q})
