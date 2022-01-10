from django import template
from django.db.models import Count, F
from ..models import Category


register = template.Library()


@register.inclusion_tag('blog/list_category.html')
def get_category():
    categories = Category.objects.all()
    return {'categories': categories}
