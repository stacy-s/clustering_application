from django.views.generic import View
from .forms import *
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import pandas as pd

# Create your views here.


class AlgorithmView(View):
    template = 'clustering/clustering.html'
    form_model = AlgorithmForm
    raise_exception = True
    df = None

    @csrf_exempt
    def get(self, request):
        form = self.form_model()
        return render(request, self.template, context={'form': form, 'is_visible': self.df is not None})

    @csrf_exempt
    def post(self, request):
        bound_form = self.form_model(request.POST, request.FILES)
        if '_upload' in request.POST and bound_form.is_valid():
            source_file = request.FILES["file"]
            self.df = pd.read_csv(source_file)
            columns = self.df.select_dtypes(include=['float', 'int']).columns
            choices = [(x, x) for x in columns]
            bound_form['latitude'].field.choices = choices
            bound_form['longitude'].field.choices = choices
            bound_form['features'].field.choices = choices
            return render(request, self.template, context={'form': bound_form, 'is_visible': self.df is not None})
        elif '_calculate' in request.POST and bound_form.is_valid():
            return render(request, self.template, context={'form': bound_form, 'is_visible': self.df is not None})
        return render(request, self.template, context={'form': bound_form, 'is_visible': self.df is not None})


