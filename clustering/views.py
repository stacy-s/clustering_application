from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .forms import *
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import plotly.express as px
from plotly.offline import plot
import k_mxt_w3


# Create your views here.

def build_2d(df, bound_form):
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
        pass
    return plt_2d


def clustering(df, bound_form):
    try:
        data_property = k_mxt_w3.data.DataPropertyImportSpace(df)
        x, y, features = data_property.get_data(name_latitude_cols=bound_form.cleaned_data['latitude'],
                                                name_longitude_cols=bound_form.cleaned_data['longitude'],
                                                features_list=bound_form.cleaned_data['features'])
        clusters = k_mxt_w3.clusters_data.ClustersDataSpaceFeaturesEuclidean(x_init=x,
                                                                             y_init=y,
                                                                             features_init=features)
        algorithm = None
        if bound_form.cleaned_data['algorithm'] == 'k_mxt_w3':
            algorithm = k_mxt_w3.clustering_algorithms.K_MXT_gauss
        elif bound_form.cleaned_data['algorithm'] == 'k_mxt':
            algorithm = k_mxt_w3.clustering_algorithms.K_MXT
        alg = algorithm(k=bound_form.cleaned_data['k'],
                        eps=bound_form.cleaned_data['eps'],
                        clusters_data=clusters)
        alg()
        fig = px.scatter_mapbox(df,
                                lat=bound_form.cleaned_data['latitude'],
                                lon=bound_form.cleaned_data['longitude'],
                                hover_name=bound_form.cleaned_data['features'][0],
                                hover_data=bound_form.cleaned_data['features'],
                                color=bound_form.cleaned_data['features'][0],
                                zoom=5,
                                height=1000,
                                color_continuous_scale=px.colors.cyclical.HSV,
                                )
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        plt_clusters = plot(fig, output_type='div', show_link=False, link_text='', )
    except Exception as e:
        pass
    return plt_clusters


class AlgorithmView(LoginRequiredMixin, View):
    template = 'clustering/clustering.html'
    form_model = FileForm
    raise_exception = True
    login_url = '/accounts/login/'
    raise_exception = False

    @csrf_exempt
    def get(self, request):
        form = self.form_model(request.GET, initial={'k': '5', 'eps': 0.05})
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
                plt_2d = build_2d(df, bound_form)
                plt_clusters = clustering(df, bound_form)
                return render(request, self.template,
                              context={'form': bound_form,
                                       'is_visible': True,
                                       'plt_2d': plt_2d,
                                       'plt_clusters': plt_clusters})
            else:
                return render(request, self.template, context={'form': bound_form, 'is_visible': True})
        return render(request, self.template, context={'form': bound_form, 'is_visible': False})
