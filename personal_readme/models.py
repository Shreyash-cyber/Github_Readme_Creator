from random import choices
from secrets import choice
from django.core.checks import messages
from django.db import models
from django.core.validators import RegexValidator
from multiselectfield import MultiSelectField
from django.utils.html import format_html
from django.utils import timezone
# Create your models here.

class SystemChoice (models.Model):
    name = models.CharField(max_length=200)
    img_link = models.URLField(blank=False)
    link = models.URLField(blank=False)

    def __str__(self):
        return format_html(f"<img class='img' src='{self.img_link}' width='50px'/><span class='hide_name' >{self.name}</span>")

class Programming_language (models.Model):
    name = models.CharField(max_length=200)
    img_link = models.URLField(blank=False)
    link = models.URLField(blank=False)

    def __str__(self):
        return format_html(f"<img class='img' src='{self.img_link}' width='50px' class='prog_lang' /><span class='hide_name' >{self.name}</span>")

class Frontend_language (models.Model):
    name = models.CharField(max_length=200)
    img_link = models.URLField(blank=False)
    link = models.URLField(blank=False)

    def __str__(self):
        return format_html(f"<img class='img' src='{self.img_link}' width='50px' /><span class='hide_name' >{self.name}</span>")

class Backend_language (models.Model):
    name = models.CharField(max_length=200)
    img_link = models.URLField(blank=False)
    link = models.URLField(blank=False)

    def __str__(self):
        return format_html(f"<img class='img' src='{self.img_link}' width='50px' /><span class='hide_name' >{self.name}</span>")

class Mobile_app_devlopment (models.Model):
    name = models.CharField(max_length=200)
    img_link = models.URLField(blank=False)
    link = models.URLField(blank=False)

    def __str__(self):
        return format_html(f"<img class='img' src='{self.img_link}' width='50px' /><span class='hide_name' >{self.name}</span>")

class AI_ML (models.Model):
    name = models.CharField(max_length=200)
    img_link = models.URLField(blank=False)
    link = models.URLField(blank=False)

    def __str__(self):
        return format_html(f"<img class='img' src='{self.img_link}' width='50px' /><span class='hide_name' >{self.name}</span>")

class Database (models.Model):
    name = models.CharField(max_length=200)
    img_link = models.URLField(blank=False)
    link = models.URLField(blank=False)

    def __str__(self):
        return format_html(f"<img class='img' src='{self.img_link}' width='50px' /><span class='hide_name' >{self.name}</span>")

class Data_visualization (models.Model):
    name = models.CharField(max_length=200)
    img_link = models.URLField(blank=False)
    link = models.URLField(blank=False)

    def __str__(self):
        return format_html(f"<img class='img' src='{self.img_link}' width='50px' /><span class='hide_name' >{self.name}</span>")

class Devops (models.Model):
    name = models.CharField(max_length=200)
    img_link = models.URLField(blank=False)
    link = models.URLField(blank=False)

    def __str__(self):
        return format_html(f"<img class='img' src='{self.img_link}' width='50px' /><span class='hide_name' >{self.name}</span>")

class BASS (models.Model):
    name = models.CharField(max_length=200)
    img_link = models.URLField(blank=False)
    link = models.URLField(blank=False)

    def __str__(self):
        return format_html(f"<img class='img' src='{self.img_link}' width='50px' /><span class='hide_name' >{self.name}</span>")

class Framework (models.Model):
    name = models.CharField(max_length=200)
    img_link = models.URLField(blank=False)
    link = models.URLField(blank=False)

    def __str__(self):
        return format_html(f"<img class='img' src='{self.img_link}' width='50px' /><span class='hide_name' >{self.name}</span>")

class Testing (models.Model):
    name = models.CharField(max_length=200)
    img_link = models.URLField(blank=False)
    link = models.URLField(blank=False)

    def __str__(self):
        return format_html(f"<img class='img' src='{self.img_link}' width='50px' /><span class='hide_name' >{self.name}</span>")

class Software (models.Model):
    name = models.CharField(max_length=200)
    img_link = models.URLField(blank=False)
    link = models.URLField(blank=False)

    def __str__(self):
        return format_html(f"<img class='img' src='{self.img_link}' width='50px' /><span class='hide_name' >{self.name}</span>")

class Static_site_gen (models.Model):
    name = models.CharField(max_length=200)
    img_link = models.URLField(blank=False)
    link = models.URLField(blank=False)

    def __str__(self):
        return format_html(f"<img class='img' src='{self.img_link}' width='50px' /><span class='hide_name' >{self.name}</span>")

class Game_engine (models.Model):
    name = models.CharField(max_length=200)
    img_link = models.URLField(blank=False)
    link = models.URLField(blank=False)

    def __str__(self):
        return format_html(f"<img class='img' src='{self.img_link}' width='50px' /><span class='hide_name' >{self.name}</span>")

class Automation (models.Model):
    name = models.CharField(max_length=200)
    img_link = models.URLField(blank=False)
    link = models.URLField(blank=False)

    def __str__(self):
        return format_html(f"<img class='img' src='{self.img_link}' width='50px' /><span class='hide_name' >{self.name}</span>")

class Blockchain (models.Model):
    name = models.CharField(max_length=200)
    img_link = models.URLField(blank=False)
    link = models.URLField(blank=False)

    def __str__(self):
        return format_html(f"<img class='img' src='{self.img_link}' width='50px' /><span class='hide_name' >{self.name}</span>")

class Others (models.Model):
    name = models.CharField(max_length=200)
    img_link = models.URLField(blank=False)
    link = models.URLField(blank=False)

    def __str__(self):
        return format_html(f"<img class='img' src='{self.img_link}' width='50px' /><span class='hide_name' >{self.name}</span>")

class Personal_readme(models.Model):
    add_on = [ 
        ('display visitors count badge', 'display visitors count badge'),
        ('display top skills', 'display top skills'),
        ('display github profile stats card','display github profile stats card')
    ]
    Link_Regex = RegexValidator(regex = "((http|https)://)(www.)?[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)")
    name = models.CharField(max_length=70, blank=False)
    about_me = models.CharField(max_length=1000, blank=True)
    resume_link = models.URLField(validators = [Link_Regex], blank=True)
    email_id = models.EmailField(blank=True)
    project1_link = models.URLField(validators = [Link_Regex], blank=True)
    project2 = models.CharField(max_length=1000, blank=True)
    project2_link = models.URLField(validators = [Link_Regex], blank=True)
    project3 = models.CharField(max_length=1000, blank=True)
    project3_link = models.URLField(validators = [Link_Regex], blank=True)
    project4 = models.CharField(max_length=1000, blank=True)
    project4_link = models.URLField(validators = [Link_Regex], blank=True)
    project5 = models.CharField(max_length=1000, blank=True)
    project5_link = models.URLField(validators = [Link_Regex], blank=True)
    work_status =  models.CharField(max_length=70, blank=True)
    work_status_link = models.URLField(validators = [Link_Regex], blank=True)
    system = models.ManyToManyField(SystemChoice, blank=True)
    programming_language = models.ManyToManyField(Programming_language, blank=True)
    frontend_language = models.ManyToManyField(Frontend_language, blank=True)
    backend_language = models.ManyToManyField(Backend_language, blank=True)
    mobile_app_devlopment = models.ManyToManyField(Mobile_app_devlopment, blank=True)
    aI_ML = models.ManyToManyField(AI_ML, blank=True)
    database = models.ManyToManyField(Database, blank=True)
    data_visualization = models.ManyToManyField(Data_visualization, blank=True)
    devops = models.ManyToManyField(Devops, blank=True)
    bASS = models.ManyToManyField(BASS, blank=True)
    framework = models.ManyToManyField(Framework, blank=True)
    testing = models.ManyToManyField(Testing, blank=True)
    software = models.ManyToManyField(Software, blank=True)
    static_site_gen = models.ManyToManyField(Static_site_gen, blank=True)
    game_engine = models.ManyToManyField(Game_engine, blank=True)
    automation = models.ManyToManyField(Automation, blank=True)
    blockchain = models.ManyToManyField(Blockchain, blank=True)
    others = models.ManyToManyField(Others, blank=True)
    github = models.URLField(validators = [Link_Regex], blank=True)
    twitter = models.URLField(validators = [Link_Regex], blank=True)
    codepen = models.URLField(validators = [Link_Regex], blank=True)
    dev = models.URLField(validators = [Link_Regex], blank=True)
    codesandbox = models.URLField(validators = [Link_Regex], blank=True)
    linkedin = models.URLField(validators = [Link_Regex], blank=True)
    kaggle = models.URLField(validators = [Link_Regex], blank=True)
    facebook = models.URLField(validators = [Link_Regex], blank=True)
    instagram = models.URLField(validators = [Link_Regex], blank=True)
    dribble = models.URLField(validators = [Link_Regex], blank=True)
    behance = models.URLField(validators = [Link_Regex], blank=True)
    hashnode = models.URLField(validators = [Link_Regex], blank=True)
    medium = models.URLField(validators = [Link_Regex], blank=True)
    youtube = models.URLField(validators = [Link_Regex], blank=True)
    codechef = models.URLField(validators = [Link_Regex], blank=True)
    hackerank = models.URLField(validators = [Link_Regex], blank=True)
    leetcode = models.URLField(validators = [Link_Regex], blank=True)
    topcoder = models.URLField(validators = [Link_Regex], blank=True)
    hackerearth = models.URLField(validators = [Link_Regex], blank=True)
    gfg = models.URLField(validators = [Link_Regex], blank=True)
    discord = models.URLField(validators = [Link_Regex], blank=True)
    rss = models.URLField(validators = [Link_Regex], blank=True)
    add_ons = MultiSelectField(choices = add_on, blank=True, max_length=300,)
    buy_me_coffee = models.URLField(validators = [Link_Regex], blank=True)

    def __str__(self):
        return format_html(f"<img class='img' src='{self.img_link}' width='50px' /><span class='hide_name' >{self.name}</span>")