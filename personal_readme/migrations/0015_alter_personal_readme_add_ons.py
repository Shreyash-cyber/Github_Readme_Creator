# Generated by Django 4.1 on 2022-09-14 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_readme', '0014_alter_personal_readme_add_ons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_readme',
            name='add_ons',
            field=models.CharField(blank=True, choices=[('Display visitors count badge', 'Display visitors count badge'), ('Display github trophy', 'Display github trophy'), ('Display top skills', 'Display top skills'), ('Display github profile stats card', 'Display github profile stats card'), ('Display github streak stats', 'Display github streak stats')], max_length=500),
        ),
    ]
