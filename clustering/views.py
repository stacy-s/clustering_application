from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import *
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def import_file(request):
    if request.method == "POST":
        file_request = request.FILES["file"]
        # errors = self.model.import_file(file_request)
        # for error in errors:
        #     messages.error(request, error)
        # if not errors:
        #     messages.success(request, _('The file import was successful!'))
        return redirect('.')
    form = UploadFileForm()
    return render(request, 'clustering/clustering.html', {'form': form})

# @csrf_exempt
# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             # file is saved
#             form.save()
#             return HttpResponseRedirect('clustering/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'clustering/clustering.html', {'form': form})
