from django import forms
from .models import *


# class UploadFileForm(forms.Form):
#     file = forms.FileField(label='file_name')


class AlgorithmForm(forms.ModelForm):
    class Meta:
        file = forms.FileField(label='file_name')
        model = Algorithm
        fields = ['file', 'k', 'eps']

        widgets = {
            'files': forms.FileField(label='file_name'),
            'k': forms.NumberInput(attrs={'class': 'form-control'}),
            'eps': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'algorithm': forms.RadioSelect(attrs={'class': 'form-control'}),
        }
