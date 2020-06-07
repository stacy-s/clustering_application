from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import *
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.





class AlgorithmView(View):
    template = 'clustering/clustering.html'
    form_model = AlgorithmForm
    model = Algorithm
    raise_exception = True
    df = None

    @csrf_exempt
    def get(self, request):
        form = self.form_model()
        return render(request, self.template, context={'form': form})

    @csrf_exempt
    def post(self, request):
        bound_form = self.form_model(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            source_file = request.FILES["file"]
            df = pd.read_csv(source_file)
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})


