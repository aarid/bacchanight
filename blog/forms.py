from django import forms
from .models import Contenir, Concerner


class AnswerForm(forms.Form):
    tag = forms.CharField(max_length=200, required=False)
    no_tag = forms.CharField(max_length=200, required=False)
    question_asked = forms.IntegerField()