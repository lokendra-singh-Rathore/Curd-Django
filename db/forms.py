from django import forms
from django.db import models
from . models import details
from django.forms import ModelForm, fields

class detailsfrom(ModelForm):
    class Meta:
        model=details
        fields='__all__'
