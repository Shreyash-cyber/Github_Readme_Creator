from django.shortcuts import render, redirect
from .forms import *
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = Personal_Readme_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('request:preview')
    else:
        form = Personal_Readme_form()
    return render(request, 'home.html', {'form': form})

def preview(request):
    return render(request, 'preview.html')