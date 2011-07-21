# -*- encoding: utf-8 -*-
from django import template
register = template.Library()

@register.filter
def cufon(value):
    print value.split(' ')
    lista = []
    for word in value.split(' '):
        palabra = '<span class="caps">%s</span>%s' % (word[0], word[1:])        
        print palabra
        lista.append(palabra)       
    return ' '.join(lista)
