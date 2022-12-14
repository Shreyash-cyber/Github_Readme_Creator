# Generated by Django 4.1 on 2022-08-31 06:15

import django.core.validators
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal_readme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('about_me', models.CharField(blank=True, max_length=100)),
                ('work_status', models.CharField(blank=True, max_length=70)),
                ('work_status_link', models.URLField(blank=True, validators=[django.core.validators.RegexValidator(regex='((http|https)://)(www.)?[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)')])),
                ('system', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('windows', 'windows'), ('linux', 'linux'), ('macOs', 'macOs'), ('unix', 'unix')], max_length=20)),
            ],
        ),
    ]
