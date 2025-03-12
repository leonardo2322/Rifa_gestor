from django import template
from decimal import Decimal

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    return value.as_widget(attrs={'class': arg})

@register.filter(name='total')
def total(value,arg):
    numeros = len(arg)
    triplete = 5
    
    if numeros == 3:
        return float(triplete) - float(value)
    elif numeros > 3 and numeros < 6:
        numero = (numeros - 3) * 2
        return 5 + numero - value
    if numeros == 6:
        return (float(triplete)* 2) - float(value)
    else:
        return len(arg) * 2 - value

@register.filter(name='replace')
def replace_comma(value):
    return str(value).replace(',', '.')