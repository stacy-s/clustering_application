from django import forms
from .models import *


class AlgorithmForm(forms.Form):
    file = forms.FileField(label='file')
    k = forms.IntegerField(label='k', widget=forms.NumberInput(attrs={'class': 'form-control'}),
                           validators=[MinValueValidator(1)],
                           required=False,
                           )
    eps = forms.FloatField(label='eps', widget=forms.NumberInput(attrs={'class': 'form-control'}),
                           validators=[MinValueValidator(0)],
                           required=False,
                           )
    latitude = forms.ChoiceField(label='latitude', choices=[('1', '1'), ('2','2')],
                               widget=forms.Select(attrs={'class': 'form-control'}),
                               required=False,
                               )
    longitude = forms.ChoiceField(label='latitude', choices=[('1', '1'), ('2', '2')],
                                 widget=forms.Select(attrs={'class': 'form-control'}),
                                 required=False,
                                  )
    features = forms.MultipleChoiceField(label='features', choices=[('1', '1'), ('2', '2')],
                                  widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
                                  required=False,
                                  )
    algorithm = forms.ChoiceField(label='algorithm', choices=[(1, 'k-MXT-W'), (2, 'k-MXT'), (3, '3-d plot'),
                                                             (3, '2-d plot')],
                                  widget=forms.Select(attrs={'class': 'form-control'}),
                                  required=False,
                                  )
