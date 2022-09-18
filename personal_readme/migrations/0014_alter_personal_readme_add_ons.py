# Generated by Django 4.1 on 2022-09-14 14:52

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('personal_readme', '0013_alter_personal_readme_add_ons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_readme',
            name='add_ons',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('first', 'Display visitors count badge'), ('second', 'Display github trophy'), ('third', 'Display top skills'), ('fourth', 'Display github profile stats card'), ('fifth', 'Display github streak stats')], max_length=500),
        ),
    ]
