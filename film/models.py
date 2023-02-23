from django.db import models
from django.urls import reverse
import urllib.parse as urlparse


class OrderByName(object):
    class Meta:
        ordering = ['name']


class SaveURLMixin(object):
    def save(self, *args, **kwarg):
        self.url = urlparse.quote_plus(str(self.name))
        super().save(*args, **kwarg)


class Director(SaveURLMixin, OrderByName, models.Model):
    name = models.CharField(max_length=200, blank=True)
    name_cn = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=200, blank=True)
    born = models.IntegerField(default=-1)
    country = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('director-detail', kwargs={'director_url': self.url})


class Actor(SaveURLMixin, OrderByName, models.Model):
    name = models.CharField(max_length=200, blank=True)
    name_cn = models.CharField(max_length=200, blank=True)
    name_alias = models.CharField(max_length=200, blank=True)
    born = models.IntegerField(default=-1)
    gender = models.CharField(max_length=200, blank=True)
    introduction = models.TextField(blank=True)
    image_file = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('actor-detail', kwargs={'actor_url': self.url})


class Studio(SaveURLMixin, OrderByName, models.Model):
    name = models.CharField(max_length=200, blank=True)
    name_cn = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('studio-detail', kwargs={'studio_url': self.url})


class Tag(SaveURLMixin, OrderByName, models.Model):
    name = models.CharField(max_length=200, blank=True)
    name_cn = models.CharField(max_length=200, blank=True)
    tag_type = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag')


class Series(SaveURLMixin, OrderByName, models.Model):
    name = models.CharField(max_length=200, blank=True)
    name_cn = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('series-detail', kwargs={'series_url': self.url})


class Film(SaveURLMixin, OrderByName, models.Model):
    name = models.CharField(max_length=200, blank=True)
    name_cn = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=200, blank=True)
    rating = models.IntegerField(default=-1)
    plot = models.TextField()
    runtime = models.IntegerField(default=-1)
    fanid = models.CharField(max_length=200, blank=True)
    tags = models.ManyToManyField(Tag, related_name='film')
    country = models.CharField(max_length=200, blank=True)
    director = models.ForeignKey(Director, blank=True, null=True, on_delete=models.SET_NULL, related_name='film')
    year = models.IntegerField(default=-1)
    studio = models.ForeignKey(Studio, blank=True, null=True, on_delete=models.SET_NULL, related_name='film')
    actors = models.ManyToManyField(Actor, related_name='film')
    film_path = models.CharField(max_length=500, blank=True)
    poster_path = models.CharField(max_length=200, blank=True)
    fanart_path = models.CharField(max_length=200, blank=True)
    series = models.ForeignKey(Series, blank=True, null=True, on_delete=models.SET_NULL, related_name='film')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('film-detail', kwargs={'film_url': self.url})
