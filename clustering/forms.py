from django import forms
from .models import *


class AlgorithmForm(forms.Form):
    file = forms.FileField(label='file')
    k = forms.IntegerField(label='k', widget=forms.NumberInput(attrs={'class': 'form-control'}),
                           validators=[MinValueValidator(1)],
                           )
    eps = forms.FloatField(label='eps', widget=forms.NumberInput(attrs={'class': 'form-control'}),
                           validators=[MinValueValidator(0)],
                           )

