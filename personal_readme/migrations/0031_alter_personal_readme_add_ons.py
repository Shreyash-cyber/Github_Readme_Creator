# Generated by Django 4.1.1 on 2022-09-17 14:27

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('personal_readme', '0030_alter_personal_readme_add_ons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_readme',
            name='add_ons',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Sandwich', 'Sandwich'), ('Salad', 'Salad'), ('omlete', 'omlete')], max_length=30, null=True),
        ),
    ]
