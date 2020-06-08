from django.views.generic import View
from .forms import *
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import plotly.express as px
from plotly.offline import plot


# Create your views here.

class AlgorithmView(View):
    template = 'clustering/clustering.html'
    form_model = FileForm
    raise_exception = True


    @csrf_exempt
    def get(self, request):
        form = self.form_model()
        return render(request, self.template, context={'form': form, 'is_visible': False})

    @csrf_exempt
    def post(self, request):
        if '_upload' in request.POST:
            self.form_model = FileForm
            bound_form = self.form_model(request.POST, request.FILES)
            if bound_form.is_valid():
                source_file = request.FILES["file"]
                df = pd.read_csv(source_file)
                columns = df.select_dtypes(include=['float', 'int']).columns
                choices = [(x, x) for x in columns]
                request.session['df'] = df.to_json()
                # request.session['choices'] = choices
                calculate_form = AlgorithmForm(choices, request.POST)
                self.form_model = AlgorithmForm
                return render(request, self.template, context={'form': calculate_form, 'is_visible': True})
        elif '_calculate' in request.POST:
            df_json = request.session.get('df', ())
            df = pd.read_json(df_json)
            columns = df.select_dtypes(include=['float', 'int']).columns
            choices = [(x, x) for x in columns]
            bound_form = AlgorithmForm(choices, request.POST)
            if bound_form.is_valid():
                try:
                    fig_2d = px.scatter_mapbox(df,
                                               lat=bound_form.cleaned_data['latitude'],
                                               lon=bound_form.cleaned_data['longitude'],
                                               hover_name=bound_form.cleaned_data['features'][0],
                                               hover_data=bound_form.cleaned_data['features'],
                                               color=bound_form.cleaned_data['features'][0],
                                               zoom=5,
                                               height=1000,
                                               color_continuous_scale=px.colors.cyclical.IceFire,
                                               )
                    fig_2d.update_layout(mapbox_style="open-street-map")
                    fig_2d.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
                    plt_2d = plot(fig_2d, output_type='div', show_link=False, link_text='', )
                except Exception as e:
                    print(e)
                return render(request, self.template, context={'form': bound_form, 'is_visible': True, 'plt_2d': plt_2d})
        return render(request, self.template, context={'form': bound_form, 'is_visible': False})
