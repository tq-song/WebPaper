from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect
from django.urls import reverse_lazy
import subprocess

from .models import Director, Actor, Studio, Tag, Series, Film
from .forms import FilmForm
from .utils import save_tags, insert_tags, add_preset_tags


class Action(generic.TemplateView):
    template_name = 'film/action.html'

def add_all():
    pass


def save_tag(request):
    save_tags()
    return redirect('action')


def insert_tag(request):
    insert_tags()
    return redirect('action')


def add_default_tag(request):
    add_preset_tags()
    return redirect('action')


class TagFilterView(generic.DetailView):
    def get_context_data(self, **kwargs):
        ctx = super(TagFilterView, self).get_context_data(**kwargs)
        films = ctx['object'].film.all().distinct()
        selected = self.request.GET.get('tags')
        if selected:
            selected = selected.split(',')
            for t in selected:
                films = films.filter(tags__name=t)
                print(films)
        tags = Tag.objects.all()
        selected_tags = tags.filter(name=selected)
        ctx['films'] = films.distinct()
        ctx['selected'] = selected
        ctx['tags'] = tags
        ctx['selected_tags'] = selected_tags
        return ctx


class FilmView(generic.ListView):
    model = Film
    # paginate_by = 20
    template_name = 'film/film.html'
    context_object_name = 'film'

    def get_context_data(self, **kwargs):
        ctx = super(FilmView, self).get_context_data(**kwargs)
        films = ctx['film']
        selected = self.request.GET.get('tags')
        selected_tags = None
        tags = Tag.objects.all()
        if selected and selected != ',':
            selected = selected.split(',')
            for t in selected:
                films = films.filter(tags__name=t)
            selected_tags = tags.filter(name__in=selected)
        ctx['films'] = films
        ctx['selected'] = selected
        ctx['tags'] = tags
        ctx['selected_tags'] = selected_tags
        return ctx


class SeriesView(generic.ListView):
    model = Series
    template_name = 'film/series.html'
    context_object_name = 'series'


class SeriesDetailView(TagFilterView):
    model = Series
    template_name = 'film/series_detail.html'

    def get_object(self):
        return get_object_or_404(Series, url=self.kwargs['series_url'])


class SeriesCreateView(generic.CreateView):
    model = Series
    fields = ['name', 'name_cn']
    template_name = 'film/public_form.html'


class SeriesUpdateView(generic.UpdateView):
    model = Series
    fields = ['name', 'name_cn']
    template_name = 'film/public_form.html'

    def get_object(self):
        return get_object_or_404(Series, url=self.kwargs['series_url'])


class SeriesDeleteView(generic.DeleteView):
    model = Series
    template_name = 'film/public_form.html'
    success_url = reverse_lazy('series')

    def get_object(self):
        return get_object_or_404(Series, url=self.kwargs['series_url'])


class DirectorView(generic.ListView):
    model = Director
    template_name = 'film/director.html'
    context_object_name = 'directors'


class DirectorDetailView(TagFilterView):
    model = Director
    template_name = 'film/director_detail.html'

    def get_object(self):
        return get_object_or_404(Director, url=self.kwargs['director_url'])


class DirectorCreateView(generic.CreateView):
    model = Director
    fields = ['name', 'name_cn', 'born', 'country']
    template_name = 'film/public_form.html'


class DirectorUpdateView(generic.UpdateView):
    model = Director
    fields = ['name', 'name_cn', 'born', 'country']
    template_name = 'film/public_form.html'

    def get_object(self):
        return get_object_or_404(Director, url=self.kwargs['director_url'])


class DirectorDeleteView(generic.DeleteView):
    model = Director
    template_name = 'film/public_form.html'
    success_url = reverse_lazy('director')

    def get_object(self):
        return get_object_or_404(Director, url=self.kwargs['director_url'])


class StudioView(generic.ListView):
    model = Studio
    template_name = 'film/studio.html'
    context_object_name = 'studio'


class StudioDetailView(TagFilterView):
    model = Studio
    template_name = 'film/studio_detail.html'

    def get_object(self):
        return get_object_or_404(Studio, url=self.kwargs['studio_url'])


class StudioCreateView(generic.CreateView):
    model = Studio
    fields = ['name', 'name_cn']
    template_name = 'film/public_form.html'


class StudioUpdateView(generic.UpdateView):
    model = Studio
    fields = ['name', 'name_cn']
    template_name = 'film/public_form.html'

    def get_object(self):
        return get_object_or_404(Studio, url=self.kwargs['studio_url'])


class StudioDeleteView(generic.DeleteView):
    model = Studio
    template_name = 'film/public_form.html'
    success_url = reverse_lazy('studio')

    def get_object(self):
        return get_object_or_404(Studio, url=self.kwargs['studio_url'])


class ActorView(generic.ListView):
    model = Actor
    template_name = 'film/actor.html'
    context_object_name = 'actor'


class ActorDetailView(TagFilterView):
    model = Actor
    template_name = 'film/actor_detail.html'

    def get_object(self):
        return get_object_or_404(Actor, url=self.kwargs['actor_url'])


class ActorCreateView(generic.CreateView):
    model = Actor
    fields = ['name', 'name_cn', 'name_alias', 'born', 'gender', 'introduction', 'image_file', 'country']
    template_name = 'film/public_form.html'


class ActorUpdateView(generic.UpdateView):
    model = Actor
    fields = ['name', 'name_cn', 'name_alias', 'born', 'gender', 'introduction', 'image_file', 'country']
    template_name = 'film/public_form.html'

    def get_object(self):
        return get_object_or_404(Actor, url=self.kwargs['actor_url'])


class ActorDeleteView(generic.DeleteView):
    model = Actor
    template_name = 'film/public_form.html'
    success_url = reverse_lazy('actor')

    def get_object(self):
        return get_object_or_404(Actor, url=self.kwargs['actor_url'])


class TagView(generic.ListView):
    model = Tag
    template_name = 'film/tag.html'
    context_object_name = 'tag'


class TagDetailView(generic.DetailView):
    model = Tag
    template_name = 'film/tag_detail.html'

    def get_object(self):
        return get_object_or_404(Tag, url=self.kwargs['tag_url'])


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ['name', 'name_cn', 'tag_type']
    template_name = 'film/public_form.html'


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ['name', 'name_cn', 'tag_type']
    template_name = 'film/public_form.html'

    def get_object(self):
        return get_object_or_404(Tag, url=self.kwargs['tag_url'])


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = 'film/public_form.html'
    success_url = reverse_lazy('tag')

    def get_object(self):
        return get_object_or_404(Tag, url=self.kwargs['tag_url'])


class FilmDetailView(generic.DetailView):
    model = Film
    template_name = 'film/film_detail.html'

    def get_object(self):
        return get_object_or_404(Film, url=self.kwargs['film_url'])


class FilmCreateView(generic.CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'film/public_form.html'

    def form_valid(self, form):
        if form.is_valid():
            saved = form.save()

        actors = form.data.get('actors').split(',')
        for a in actors:
            if not Actor.objects.filter(name=a).exists():
                this_a = Actor(name=a)
                this_a.save()
        for a in Actor.objects.filter(name__in=actors):
            if not saved.actors.filter(name=a).exists():
                saved.actors.add(a)

        tags = form.data.get('tags').split(',')
        for a in tags:
            if not Tag.objects.filter(name=a).exists():
                this_a = Tag(name=a)
                this_a.save()
        for a in Tag.objects.filter(name__in=tags):
            if not saved.tags.filter(name=a).exists():
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


class FilmUpdateView(generic.UpdateView):
    model = Film
    form_class = FilmForm
    template_name = 'film/public_form.html'

    def get_object(self):
        return get_object_or_404(Film, url=self.kwargs['film_url'])

    def get_initial(self):
        initial = super(FilmUpdateView, self).get_initial()
        initial['actors'] = ','.join([a.name for a in self.object.actors.all()])
        initial['tags'] = ','.join([a.name for a in self.object.tags.all()])
        series = self.object.series
        if series:
            initial['series'] = self.object.series.name
        studio = self.object.studio
        if studio:
            initial['studio'] = self.object.studio.name
        director = self.object.director
        if director:
            initial['director'] = self.object.director.name
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


class FilmDeleteView(generic.DeleteView):
    model = Film
    template_name = 'film/public_form.html'
    success_url = reverse_lazy('tag')

    def get_object(self):
        return get_object_or_404(Film, url=self.kwargs['film_url'])


def add_player(request, film_url):
    cmd = 'PotPlayerMini64.exe /add f:/11_资料/kodi/'
    film = Film.objects.get(url=film_url)
    files = film.film_path.split(',')
    for f in files:
        this_cmd = cmd + f
        subprocess.run(this_cmd)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def add_one_tag(request, film_url):
    f = Film.objects.get(url=film_url)
    tags = Tag.objects.all()
    if request.method == 'POST':
        this_tag_name = request.POST['tags']
        this_tag = Tag.objects.get(name=this_tag_name)
        selected_tags = [a[0] for a in f.tags.values_list('name')]
        if this_tag_name in selected_tags:
            f.tags.remove(this_tag)
        else:
            f.tags.add(this_tag)
    return render(request, 'film/add_one_tag.html', {'film': f, 'tags': tags})