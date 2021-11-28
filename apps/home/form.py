from django import forms
from django.contrib.auth.models import User
from django.forms.fields import DateField

from .models import ProfilDetay


class ProfilDetayForm(forms.ModelForm):

    class Meta:
        model = ProfilDetay
        fields = ('__all__')

    
