# Generated by Django 5.0.6 on 2024-06-30 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_job_posted_by_alter_job_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='job',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='applicant',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='user',
        ),
        migrations.DeleteModel(
            name='Job',
        ),
        migrations.DeleteModel(
            name='JobApplication',
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
