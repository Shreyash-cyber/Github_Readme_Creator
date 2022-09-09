from typing import ClassVar
from django import forms
from django.forms import ModelForm, Textarea, fields, widgets
from .models import *

class Personal_Readme_form(forms.ModelForm):
    class Meta:
        model = Personal_readme
        fields = '__all__'
        labels = {
            'name':'Your Name',
            'about':'About Yourself',
            'work_status':'Your Current work status',
            'resume_link':'Your Resume',
            'work_status':'Your current status',
            'system':'I prefer working on',
            'programming_language':'Programming Languages',
            'frontend_language':'Frontend Languages',
            'backend_language':'Backend Languages',
            'mobile_app_devlopment':'Mobile App Devlopment',
            'aI_ML':'AI/ML',
            'database':'Database',
            'data_visualization':'Data Visualization',
            'devops':'Devops',
            'bASS':'Backend as a service (BaaS)',
            'framework':'Framework',
            'testing':'Testing',
            'software':'Software',
            'static_site_gen':'Static Site Genrators',
            'game_engine':'Game Engine',
            'automation':'Automation',
            'blockchain':'Blockchain',
            'others':"Others",
            'github':'Github',
            'twitter':'Twitter',
            'codepen':"Codepen",
            'dev':'Dev',
            'codesandbox':'Codesandbox',
            'linkedin':'Linkedin',
            'kaggle':'Kaggle',
            'facebook':'Facebook',
            'instagram':'Instagram',
            'dribble':'Dribble',
            'behance':'Behance',
            'hashnode':'Hashnode',
            'medium':'Medium',
            'youtube':'Youtube',
            'codechef':'Codechef',
            'hackerank':'Hackerrank',
            'leetcode':'Leetcode',
            'topcoder':'Topcoder',
            'hackerearth':'Hackerearth',
            'gfg':'GFG',
            'discord':'Discord',
            'rss':'RSS',
            'add_ons':'Add Ons',
            'buy_me_coffee':'Buy me coffee'
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Type your name','id':'name'}),
            'about_me': forms.Textarea(attrs={'placeholder': 'A short summary about yourself'}),

            'project1': forms.TextInput(attrs={'placeholder':'Name of your project'}),
    
            'project2': forms.TextInput(attrs={'placeholder':'Name of your project'}),
    
            'project3': forms.TextInput(attrs={'placeholder':'Name of your project'}),
    
            'project4': forms.TextInput(attrs={'placeholder':'Name of your project'}),
    
            'project5': forms.TextInput(attrs={'placeholder':'Name of your project'}),
    
            'work_status' : forms.TextInput(attrs={'placeholder': 'Your current status'}),

            'system' : forms.CheckboxSelectMultiple(attrs={'id':'system'}),
            'programming_language' : forms.CheckboxSelectMultiple(attrs={'id':'programming_language'}),
            'frontend_language' : forms.CheckboxSelectMultiple(attrs={'id':'frontend_language'}),
            'backend_language' : forms.CheckboxSelectMultiple(attrs={'id':'backend_language'}),
            'mobile_app_devlopment' : forms.CheckboxSelectMultiple(attrs={'id':'mobile_app_devlopment'}),
            'aI_ML' : forms.CheckboxSelectMultiple(attrs={'id':'aI_ML'}),
            'database' : forms.CheckboxSelectMultiple(attrs={'id':'database'}),
            'data_visualization' : forms.CheckboxSelectMultiple(attrs={'id':'data_visualization'}),
            'devops' : forms.CheckboxSelectMultiple(attrs={'id':'devops'}),
            'bASS' : forms.CheckboxSelectMultiple(attrs={'id':'bASS'}),
            'framework' : forms.CheckboxSelectMultiple(attrs={'id':'framework'}),
            'testing' : forms.CheckboxSelectMultiple(attrs={'id':'testing'}),
            'software' : forms.CheckboxSelectMultiple(attrs={'id':'software'}),
            'static_site_gen' : forms.CheckboxSelectMultiple(attrs={'id':'static_site_gen'}),
            'game_engine' : forms.CheckboxSelectMultiple(attrs={'id':'game_engine'}),
            'automation' : forms.CheckboxSelectMultiple(attrs={'id':'automation'}),
            'blockchain' : forms.CheckboxSelectMultiple(attrs={'id':'blockchain'}),
            'others' : forms.CheckboxSelectMultiple(attrs={'id':'others'}),
            'add_ons':forms.CheckboxSelectMultiple(attrs={'id':'add_ons'}),            
        }