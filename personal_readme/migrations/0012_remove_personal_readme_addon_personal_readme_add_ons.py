# Generated by Django 4.1 on 2022-09-14 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_readme', '0011_alter_personal_readme_addon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal_readme',
            name='addon',
        ),
        migrations.AddField(
            model_name='personal_readme',
            name='add_ons',
            field=models.CharField(blank=True, choices=[('first', 'Display visitors count badge'), ('second', 'Display github trophy'), ('third', 'Display top skills'), ('fourth', 'Display github profile stats card'), ('fifth', 'Display github streak stats')], max_length=500),
        ),
    ]
