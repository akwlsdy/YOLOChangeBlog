# Generated by Django 5.1.4 on 2024-12-16 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicesystem', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_file',
        ),
    ]
