from django import forms
from cowsay.models import CowsText

class CowsTextForm(forms.Form):
    text = forms.CharField(max_length=500)
