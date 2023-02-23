import this
from django import template
from ..models import Film

register = template.Library()

@register.filter(name='tag_type')
def tag_type(value):
    types = list(set([a[0] for a in value.values_list('tag_type')]))
    return types

@register.filter(name='sub_tags')
def sub_tags(value, this_type):
    value = value.filter(tag_type=this_type)
    return value

@register.filter(name='add_suffix')
def add_suffix(value):
    if value.endswith('/'):
        value += '?tags='
    else:
        value += ','
    return value

@register.filter(name='remove_tag')
def remove_tag(selected, this_tag):
    tags = selected.copy()
    tags.remove(this_tag)
    if not tags:
        ret = ''
    else:
        ret = '?tags=' + ','.join(tags)
    return ret

@register.filter(name='next_film')
def next_film(value, this_film):
    temp = Film.objects.filter(name__gt=this_film.name)
    if temp.exists():
        ret = temp.order_by('name').first().url
    else:
        ret = this_film.url
    return ret
