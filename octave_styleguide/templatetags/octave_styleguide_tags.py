from django import template
from django.conf import settings

from lib.octave_styleguide.octave_styleguide.utils import get_styleguide_menu

register = template.Library()


@register.inclusion_tag('tags/styleguide_menu.html')
def styleguide_menu():
    return {
        'menu': get_styleguide_menu(),
        'debug': settings.DEBUG,
    }
