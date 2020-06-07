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
        return render(request, self.template, context={'form': form})

    @csrf_exempt
    def post(self, request):
        bound_form = self.form_model(request.POST, request.FILES)
        if bound_form.is_valid():
            source_file = request.FILES["file"]
            df = pd.read_csv(source_file)
            return render(request, self.template, context={'form': bound_form})
        return render(request, self.template, context={'form': bound_form})


