from django import forms


class AnswerForm(forms.Form):
    reponse = forms.CharField(max_length=200)