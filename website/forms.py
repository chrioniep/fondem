from django import forms
from .models import Event


class DashboardForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs=({'placeholder':'Titre'})))
    content = forms.CharField(widget=forms.Textarea(attrs=({'rows':"15", 'cols':"6", 'placeholder':"Contenue"})))


