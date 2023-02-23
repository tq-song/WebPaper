from .models import Tag

def get_all_parents(t):
    tag = Tag.objects.get(name=t)
    tags = [tag.name]
    while tag.parent:
        tag = tag.parent
        tags.append(tag.name)
    return tags