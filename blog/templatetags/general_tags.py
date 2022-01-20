from django import template
from django.db.models import Count, F
from blog.models import Post, Project, Technology


register = template.Library()


@register.inclusion_tag('blog/index_include/most_post.html')
def get_posts():
    posts = Post.objects.all().select_related().annotate(most_popular_posts=F('views'))
    return {'posts': posts, }


@register.simple_tag
def get_projects():
    return Project.objects.all()


@register.inclusion_tag('blog/index_include/most_used_tchs.html')
def get_most_used_tchs(lim=4):
    most_used_tchs = Technology.objects.annotate(cnt=Count('project')).order_by('-cnt')[:lim]
    return {'most_used_tchs': most_used_tchs}
