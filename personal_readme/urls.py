from django.urls import path
from .views import *
from . import views

app_name = 'personal_readme'

urlpatterns = [
    path('',views.home,name='home'),
]