# Generated by Django 4.1 on 2022-09-16 06:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('personal_readme', '0020_alter_personal_readme_add_ons'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_readme',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
