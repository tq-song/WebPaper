from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect
from django.urls import reverse_lazy

from .models import Author, Journal, Tag, Paper


class PaperView(generic.ListView):
    model = Paper
    template_name = 'paper/paper.html'