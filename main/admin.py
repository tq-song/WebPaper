from django.contrib import admin

from .models import Author, Journal, Tag, Paper

# Register your models here.
admin.site.register(Author)
admin.site.register(Journal)
admin.site.register(Tag)
admin.site.register(Paper)