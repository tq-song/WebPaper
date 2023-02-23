from django.contrib import admin

from .models import Director, Actor, Studio, Tag, Series, Film


admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Studio)
admin.site.register(Tag)
admin.site.register(Series)
admin.site.register(Film)