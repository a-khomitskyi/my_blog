from django import template
from blog.models import Post, Project, Category


register = template.Library()


@register.simple_tag
def get_posts():
    return Post.objects.all().select_related()


@register.simple_tag
def get_projects():
    return Project.objects.all().prefetch_related()
