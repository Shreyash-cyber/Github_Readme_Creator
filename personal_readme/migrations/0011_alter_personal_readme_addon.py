# Generated by Django 4.1 on 2022-09-14 14:39

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('personal_readme', '0010_rename_add_ons_personal_readme_addon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_readme',
            name='addon',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('first', 'first'), ('second', 'Display github trophy'), ('third', 'Display top skills'), ('fourth', 'Display github profile stats card'), ('fifth', 'Display github streak stats')], max_length=500),
        ),
    ]
