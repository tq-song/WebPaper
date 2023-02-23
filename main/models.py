from django.db import models
from django.urls import reverse

class OrderByTitle(object):
    class Meta:
        ordering = ['title']


class Author(OrderByTitle, models.Model):
    name = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=200, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'author_url': self.url})


class Journal(OrderByTitle, models.Model):
    name = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=200, blank=True)

    def get_absolute_url(self):
        return reverse('journal-detail', kwargs={'journal_url': self.url})


class Tag(OrderByTitle, models.Model):
    name = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=200, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL, related_name='children')

    def get_absolute_url(self):
        return reverse('tag')


class Paper(OrderByTitle, models.Model):
    name = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=200, blank=True)
    abstract = models.TextField()
    authors = models.ManyToManyField(Author, related_name='papers')
    tags = models.ManyToManyField(Tag, related_name='papers')
    journal = models.ForeignKey(Journal, blank=True, null=True, on_delete=models.SET_NULL, related_name='papers')
    comment = models.TextField()
    year = models.IntegerField(default=-1)

    def get_absolute_url(self):
        return reverse('paper-detail', kwargs={'paper_url': self.url})
