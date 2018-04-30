from django import forms
from django.apps import apps
from django.core.exceptions import ValidationError
from .models import Diagram


class ModelerForm(forms.Form):

    # def __init__(self, *args, **kwargs):

    #     name = kwargs.pop('name')
    #     content = kwargs.pop('content')

    #     super(ModelerForm, self).__init__(*args, **kwargs)

    # Fields:
    #(widget=forms.HiddenInput())

    name = forms.CharField(label='Name', required=True)
    content = forms.CharField(widget=forms.HiddenInput, label='Content', required=True)
    svg_content = forms.CharField(widget=forms.HiddenInput, label='Content', required=True)

    def __repr__(self):
        return 'ModelerForm: '




