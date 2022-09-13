from django.shortcuts import render, redirect
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

def preview(request):
    readme = Personal_readme.objects.all()
    return render(request, 'preview.html',{'readme':readme})