# Generated by Django 5.0.6 on 2024-06-07 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_document_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='user',
        ),
    ]
