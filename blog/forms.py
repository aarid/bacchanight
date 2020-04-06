from django import forms
from .models import Contenir, Concerner


class AnswerForm(forms.Form):
    tag = forms.CharField(max_length=200, required=False)
    no_tag = forms.CharField(max_length=200, required=False)
    question_asked = forms.CharField(max_length=100, required=False)

class ContacterNous(forms.Form):
    nomPrenom = forms.CharField(max_length=100)
    admail = forms.EmailField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender  = forms.CharField()
    cc_myself = forms.BooleanField(required=False)
