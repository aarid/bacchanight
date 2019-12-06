from django import forms


class AnswerForm(forms.Form):
    bidule = forms.CharField(max_length=100)