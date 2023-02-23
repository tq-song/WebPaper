from django import template
from ..models import Paper, Tag
from ..utils import get_all_parents

register = template.Library()

@register.filter(name='remove_tag')
def remove_tag(selected, this_tag):
    tags = selected.copy()
    tags.remove(this_tag)
    if not tags:
        ret = ''
    else:
        ret = '?tags=' + ','.join(tags)
    return ret

@register.simple_tag
def add_suffix(url, tag):
    if url.endswith('/'):
        url += '?tags='
        tags = get_all_parents(tag)
        url = url + ','.join(tags)
    else:
        pass # to be done
    return url