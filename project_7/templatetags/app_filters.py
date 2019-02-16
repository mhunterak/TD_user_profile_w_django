from django import template

register = template.Library()


@register.filter(name='display_clean')
def display_clean(value):
    '''
When used with | title,
helps to display profile attributes
    '''
    value_array = value.split('_')
    return " ".join(value_array)
