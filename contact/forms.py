# -*- coding: UTF-8 -*-
from django import forms as forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    #phone = forms.CharField(max_length=20)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
