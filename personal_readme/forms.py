from typing import ClassVar
from django import forms
from django.forms import ModelForm, Textarea, fields, widgets
from .models import *

class Personal_Readme_form(forms.ModelForm):
    class Meta:
        model = Personal_readme
        fields = '__all__'
        labels = {
            'name':'Your Name',
            'about':'About',
            'work_status':'Your Current work status',
            'system':'I preffered to work with'
        }