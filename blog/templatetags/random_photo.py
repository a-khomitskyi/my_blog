from django import template
import random


register = template.Library()


@register.simple_tag
def get_random_photo_url():
    prefix = 'img-'
    suffix = '.jpg'
    return 'images/' + prefix + str(random.randint(1, 6)) + suffix
