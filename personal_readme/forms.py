from typing import ClassVar
from django import forms
from django.forms import ModelForm, Textarea, fields, widgets
from django.core.exceptions import ValidationError
from .models import *

class Personal_Readme_form(ModelForm):
    class Meta:
        model = Personal_readme
        fields = '__all__'

        def clean(self):
            cleaned_data = super().clean()
            github = cleaned_data.get("github")
            add_ons = cleaned_data.get("add_ons")

            if len(add_ons) > 0  and add_ons!= '' and  github == '':
                raise ValidationError(
                    "fill in github username"
                )

        labels = {
            'name':'Your Name',
            'about':'About Yourself',
            'work_status':'Your Current work status',
            'resume_link':'Your Resume',
            'work_status':'Your current status',
            'system':'I prefer working on',
            'project1_link': 'Your portfolio link',
            'project2':'I am currently working on',
            'project3':'I am looking to collaborate on',
            'project4':'I am looking for help with',
            'project5':'My favourite project',
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
            'linkedin':'Linkedin',
            'kaggle':'Kaggle',
            'facebook':'Facebook',
            'instagram':'Instagram',
            'dribble':'Dribble',
            'behance':'Behance',
            'hashnode':'Hashnode',
            'medium':'Medium',
            'youtube':'Youtube',
            'hackerank':'Hackerrank',
            'leetcode':'Leetcode',
            'topcoder':'Topcoder',
            'hackerearth':'Hackerearth',
            'discord':'Discord',
            'rss':'RSS',
            'add_ons':'Add Ons',
            'buy_me_coffee':'Buy me coffee',
            'patreon':'Patreon',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '  type your name','id':'name','font-size':'50px'}),
            'about_me': forms.TextInput(attrs={'placeholder': '  a short summary about yourself','id':'about_me'}),
            'resume_link': forms.TextInput(attrs={'placeholder':' link of your resume','id':'resume_link'}),
            'email_id': forms.EmailInput(attrs={'placeholder':'  your email id','id':'email_id'}),
            'project1_link': forms.TextInput(attrs={'placeholder':'  link of your portfolio/website','id':'project1_link'}),
            'project2': forms.TextInput(attrs={'placeholder':'  project name','id':'project2'}),
            'project2_link': forms.TextInput(attrs={'placeholder':'  link of your project/github repo','id':'project2_link'}),
            'project3': forms.TextInput(attrs={'placeholder':'  project name','id':'project3'}),
            'project3_link': forms.TextInput(attrs={'placeholder':'  link of your project/github repo','id':'project3_link'}),
            'project4': forms.TextInput(attrs={'placeholder':'  project name','id':'project4'}),
            'project4_link': forms.TextInput(attrs={'placeholder':'  link of your project/github repo','id':'project4_link'}),
            'project5': forms.TextInput(attrs={'placeholder':'  project name','id':'project5'}),
            'project5_link': forms.TextInput(attrs={'placeholder':'  link of your project/github repo','id':'project5_link'}),
            'work_status' : forms.TextInput(attrs={'placeholder':'  Student, Software developer, UI/UX designer,  Tester','id':'work_status'}),
            'work_status_link' : forms.TextInput(attrs={'placeholder':'  link of current working oraganization if any','id':'work_status_link'}),
            'system' : forms.CheckboxSelectMultiple(attrs={'class':'system'}),
            'programming_language' : forms.CheckboxSelectMultiple(attrs={'class':'programming_language'}),
            'frontend_language' : forms.CheckboxSelectMultiple(attrs={'class':'frontend_language'}),
            'backend_language' : forms.CheckboxSelectMultiple(attrs={'class':'backend_language'}),
            'mobile_app_devlopment' : forms.CheckboxSelectMultiple(attrs={'class':'mobile_app_devlopment'}),
            'aI_ML' : forms.CheckboxSelectMultiple(attrs={'class':'aI_ML'}),
            'database' : forms.CheckboxSelectMultiple(attrs={'class':'database'}),
            'data_visualization' : forms.CheckboxSelectMultiple(attrs={'class':'data_visualization'}),
            'devops' : forms.CheckboxSelectMultiple(attrs={'class':'devops'}),
            'bASS' : forms.CheckboxSelectMultiple(attrs={'class':'bASS'}),
            'framework' : forms.CheckboxSelectMultiple(attrs={'class':'framework'}),
            'testing' : forms.CheckboxSelectMultiple(attrs={'class':'testing'}),
            'software' : forms.CheckboxSelectMultiple(attrs={'class':'software'}),
            'static_site_gen' : forms.CheckboxSelectMultiple(attrs={'class':'static_site_gen'}),
            'game_engine' : forms.CheckboxSelectMultiple(attrs={'class':'game_engine'}),
            'automation' : forms.CheckboxSelectMultiple(attrs={'class':'automation'}),
            'blockchain' : forms.CheckboxSelectMultiple(attrs={'class':'blockchain'}),
            'others' : forms.CheckboxSelectMultiple(attrs={'class':'others'}),  
            'github': forms.TextInput(attrs={'placeholder':'  github username','id':'github'}),
            'twitter': forms.TextInput(attrs={'placeholder':'  link of your twitter profile','id':'twitter'}),
            'codepen': forms.TextInput(attrs={'placeholder':'  link of your codepen profile','id':'codepen'}),
            'dev': forms.TextInput(attrs={'placeholder':'  link of your dev profile','id':'dev'}),
            'linkedin': forms.TextInput(attrs={'placeholder':'  link of your linkedin profile','id':'linkedin'}),
            'kaggle': forms.TextInput(attrs={'placeholder':'  link of your kaggle profile','id':'kaggle'}),
            'facebook': forms.TextInput(attrs={'placeholder':'  link of your facebook profile','id':'facebook'}),
            'instagram': forms.TextInput(attrs={'placeholder':'  link of your instagram profile','id':'instagram'}),
            'dribble': forms.TextInput(attrs={'placeholder':'  link of your dribble profile','id':'dribble'}),
            'behance': forms.TextInput(attrs={'placeholder':'  link of your behance profile','id':'behance'}),
            'hashnode': forms.TextInput(attrs={'placeholder':'  link of your hashnode profile','id':'hashnode'}),
            'medium': forms.TextInput(attrs={'placeholder':'  link of your medium page','id':'medium'}),
            'youtube': forms.TextInput(attrs={'placeholder':'  link of your youtube channel','id':'youtube'}),
            'hackerank': forms.TextInput(attrs={'placeholder':'  link of your hackerrank profile','id':'hackerank'}),
            'leetcode': forms.TextInput(attrs={'placeholder':'  link of your leetcode profile','id':'leetcode'}),
            'topcoder': forms.TextInput(attrs={'placeholder':'  link of your topcoder profile','id':'topcoder'}),
            'hackerearth': forms.TextInput(attrs={'placeholder':'  link of your hackerearth profile','id':'hackerearth'}),
            'discord': forms.TextInput(attrs={'placeholder':'  link of your discord profile','id':'discord'}),
            'rss': forms.TextInput(attrs={'placeholder':'  rss feed URL','id':'rss'}),
            'add_ons' : forms.CheckboxSelectMultiple(attrs={'id': 'add_ons'}),
            'buy_me_coffee': forms.TextInput(attrs={'placeholder':'  link of your buy me coffee page','id':'buy_me_coffee'}),
            'patreon': forms.TextInput(attrs={'placeholder':'   link of your patreon page','id':'patreon'}),
        }