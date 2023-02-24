from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect
from django.urls import reverse_lazy

from .models import Author, Journal, Tag, Paper
from .forms import PaperForm


class PaperView(generic.ListView):
    model = Paper
    template_name = 'paper/paperlist.html'
    context_object_name = 'paper'

    def get_context_data(self, **kwargs):
        ctx = super(PaperView, self).get_context_data(**kwargs)
        papers = ctx['papers']
        selected = self.request.GET.get('tags')
        selected_tags = None
        tags = Tag.objects.all()
        if selected and selected != ',':
            selected = selected.split(',')
            for t in selected:
                papers = papers.filter(tags__name=t)
            selected_tags = tags.filter(name__in=selected)
        ctx['papers'] = papers
        ctx['selected'] = selected
        ctx['tags'] = tags
        ctx['selected_tags'] = selected_tags
        return ctx
    

class AuthorView(generic.ListView):
    model = Author
    template_name = 'paper/author.html'
    context_object_name = 'authors'


class AuthorDetailView():
    model = Author
    template_name = 'paper/author_detail.html'

    def get_object(self):
        return get_object_or_404(Author, url=self.kwargs['author_url'])


class AuthorDeleteView(generic.DeleteView):
    model = Author
    template_name = 'paper/public_form.html'
    success_url = reverse_lazy('author')

    def get_object(self):
        return get_object_or_404(Author, url=self.kwargs['author_url'])


class JournalView(generic.ListView):
    model = Journal
    template_name = 'paper/journal.html'
    context_object_name = 'journals'


class JournalDetailView():
    model = Journal
    template_name = 'paper/journal_detail.html'

    def get_object(self):
        return get_object_or_404(Journal, url=self.kwargs['journal_url'])


class JournalDeleteView(generic.DeleteView):
    model = Journal
    template_name = 'paper/public_form.html'
    success_url = reverse_lazy('journal')

    def get_object(self):
        return get_object_or_404(Journal, url=self.kwargs['journal_url'])


class TagView(generic.ListView):
    model = Tag
    template_name = 'paper/tag.html'
    context_object_name = 'tag'


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = 'paper/public_form.html'
    success_url = reverse_lazy('tag')

    def get_object(self):
        return get_object_or_404(Tag, url=self.kwargs['tag_url'])


class PaperDetailView(generic.DetailView):
    model = Paper
    template_name = 'paper/paper_detail.html'

    def get_object(self):
        return get_object_or_404(Paper, url=self.kwargs['paper_url'])


class PaperCreateView(generic.CreateView):
    model = Paper
    form_class = PaperForm
    template_name = 'paper/public_form.html'

    def form_valid(self, form):
        if form.is_valid():
            saved = form.save()

        authors = form.data.get('authors').split(';')
        for a in authors:
            if not Author.objects.filter(name=a).exists():
                this_a = Author(name=a)
                this_a.save()
        for a in Author.objects.filter(name__in=authors):
            if not saved.authors.filter(name=a).exists():
                saved.authors.add(a)

        tags = form.data.get('tags').split(',')
        for a in tags:
            if not Tag.objects.filter(name=a).exists():
                this_a = Tag(name=a)
                this_a.save()
        for a in Tag.objects.filter(name__in=tags):
            if not saved.tags.filter(name=a).exists():
                saved.tags.add(a)

        return super().form_valid(form)


class PaperUpdateView(generic.UpdateView):
    model = Paper
    form_class = PaperForm
    template_name = 'paper/public_form.html'

    def get_object(self):
        return get_object_or_404(Paper, url=self.kwargs['paper_url'])

    def get_initial(self):
        initial = super(PaperUpdateView, self).get_initial()
        initial['authors'] = ','.join([a.name for a in self.object.authors.all()])
        initial['tags'] = ','.join([a.name for a in self.object.tags.all()])
        journal = self.object.journal
        if journal:
            initial['journal'] = self.object.journal.name
        return initial
    
    def form_valid(self, form):
        if form.is_valid():
            saved = form.save()

        actors = form.data.get('actors').split(',')
        for a in actors:
            if not Actor.objects.filter(name=a).exists():
                this_a = Actor(name=a)
                this_a.save()
        saved.actors.clear()
        for a in Actor.objects.filter(name__in=actors):
            saved.actors.add(a)

        tags = form.data.get('tags').split(',')
        for a in tags:
            if not Tag.objects.filter(name=a).exists():
                this_a = Tag(name=a)
                this_a.save()
        saved.tags.clear()
        for a in Tag.objects.filter(name__in=tags):
            saved.tags.add(a)

        this_series = form.data.get('series')
        if not Series.objects.filter(name=this_series):
            this_a = Series(name=this_series)
            this_a.save()
        saved.series = Series.objects.get(name=this_series)

        this_director = form.data.get('director')
        if not Director.objects.filter(name=this_director):
            this_a = Director(name=this_director)
            this_a.save()
        saved.director = Director.objects.get(name=this_director)

        this_studio = form.data.get('studio')
        if not Studio.objects.filter(name=this_studio):
            this_a = Studio(name=this_studio)
            this_a.save()
        saved.studio = Studio.objects.get(name=this_studio)

        return super().form_valid(form)


class PaperDeleteView(generic.DeleteView):
    model = Paper
    template_name = 'paper/public_form.html'
    success_url = reverse_lazy('tag')

    def get_object(self):
        return get_object_or_404(Paper, url=self.kwargs['paper_url'])
