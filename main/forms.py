from django import forms

from .models import Author, Journal, Tag, Paper


class PaperForm(forms.ModelForm):
    authors = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':3, 'cols':30}))
    journal = forms.CharField(required=False)
    tags = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':3, 'cols':30}))

    class Meta:
        model = Film
        fields = ['name', 'abstract', 'year', 'comment']