from django.core.checks import messages
from django.db import models
from django.core.validators import RegexValidator
from multiselectfield import MultiSelectField
from django.utils import timezone
# Create your models here.

class Personal_readme(models.Model):
    system_choice = [
        ('windows', 'windows'),
        ('linux', 'linux'),
        ('macOs', 'macOs'),
        ('unix', 'unix')
    ]
    work_status_Regex = RegexValidator(regex = "((http|https)://)(www.)?[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)")
    name = models.CharField(max_length=70, blank=False)
    about_me = models.CharField(max_length=100, blank=True)
    work_status =  models.CharField(max_length=70, blank=True)
    work_status_link = models.URLField(validators = [work_status_Regex], blank=True)
    system = MultiSelectField(max_length=20, choices=system_choice,max_choices=4, blank=True )


    def __str__(self):
        return self.name