from django import forms
from django.db import models

from .models import Director, Actor, Studio, Tag, Series, Film


class FilmForm(forms.ModelForm):
    actors = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':3, 'cols':30}))
    director = forms.CharField(required=False)
    studio = forms.CharField(required=False)
    series = forms.CharField(required=False)
    tags = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':3, 'cols':30}))

    class Meta:
        model = Film
        fields = ['name', 'name_cn', 'rating', 'plot', 'runtime', 'fanid', 'country', 'year', 'film_path', 'poster_path', 'fanart_path']

