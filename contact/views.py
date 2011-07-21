# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from forms import *

def index(request):
        
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            #phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            contenido = render_to_string('contact/message.txt', RequestContext(request, locals()))
            send_mail('Contaco desde Cieets.org.ni', contenido, 'no-reply@cieets.org.ni', ['cieets@cieets.org.ni', 'biblioteca@cieets.org.ni'])
            return HttpResponseRedirect('/contact/?status=ok')
    else:
        form = ContactForm()
        status = request.GET.get('status', '')
    return render_to_response('contact/index.html', RequestContext(request, locals()))
