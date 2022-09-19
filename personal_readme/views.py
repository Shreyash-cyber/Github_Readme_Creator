from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from .forms import *
from .models import *
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = Personal_Readme_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('personal_readme:preview')
    else:
        form = Personal_Readme_form()
    return render(request, 'home.html', {'form': form})

def get_referer(request):
    referer = request.META.get('HTTP_REFERER')
    if not referer:
        return None
    return referer

def preview(request):
    if not get_referer(request):
        raise Http404
    readme = [Personal_readme.objects.latest('create_date')]
    return render(request, 'preview.html',{'readme':readme})