from django import template
from phonebook.models import *

register = template.Library()

@register.simple_tag()
def get_division():
    return Division.objects.all()

