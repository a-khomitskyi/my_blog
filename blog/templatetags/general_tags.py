from django import template
from django.db.models import Count
from blog.models import Post, Project, Category, Technology


register = template.Library()


@register.inclusion_tag('blog/index_include/most_post.html')
def get_posts():
    posts = Post.objects.all().select_related()
    most_popular_posts= posts.order_by('-views')[:4]
    recent_posts = posts.order_by('-created_at')[:4]
    return {'most_popular_posts': most_popular_posts, 'recent_posts': recent_posts}


@register.simple_tag
def get_projects():
    return Project.objects.all()


@register.inclusion_tag('blog/index_include/most_used_tchs.html')
def get_most_used_tchs(lim=4):
    most_used_tchs = Technology.objects.annotate(cnt=Count('project')).order_by('-cnt')[:lim]
    return {'most_used_tchs': most_used_tchs}
