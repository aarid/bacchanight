from django import forms
from .models import Contenir, Concerner


class AnswerForm(forms.Form):
    reponse = forms.CharField(max_length=200, required=False)