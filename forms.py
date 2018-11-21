from django import forms
from .models import blog

class blogForm(forms.Form):
    title = forms.CharField(label="title")
    image = forms.FileField(label="image")
    content = forms.CharField(label="content")
    create_date = forms.DateTimeField(label="date")
