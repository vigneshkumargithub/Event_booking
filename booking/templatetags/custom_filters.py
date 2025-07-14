from django import template

register = template.Library()

@register.filter
def seats_left(event):
    return event.seats_left()