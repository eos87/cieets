# -*- encoding: utf-8 -*-
from django import template
register = template.Library()

@register.filter
def cufon(value):
    print value.split(' ')
    lista = []
    for word in value.split(' '):
        if len(word) > 0:
            palabra = u'<span class="caps">%s</span>%s' % (word[0], word[1:])
            lista.append(palabra)       
    return ' '.join(lista)
