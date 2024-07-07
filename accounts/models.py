from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.db.models.signals import post_save
from django.dispatch import receiver
# import datetime
# from django.conf import settings

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    technical_skills = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    account_type = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    telegram = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    x = models.URLField(null=True, blank=True)  # Consider renaming this field to be more descriptive
    linkedin = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    spoken_languages = models.CharField(max_length=255, null=True, blank=True)
    available_for_work_from_date = models.DateField(null=True, blank=True)
    preferred_annual_pay = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    preferred_hourly_pay = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    
    # New fields for job hirers
    company_name = models.CharField(max_length=255, null=True, blank=True)
    designation = models.CharField(max_length=255, null=True, blank=True)
    company_description = models.TextField(null=True, blank=True)
    company_stage = models.CharField(max_length=255, null=True, blank=True)
    product_service = models.TextField(null=True, blank=True)
    company_photo = models.ImageField(upload_to='company_photos/', null=True, blank=True)
    working_email = models.EmailField(default='default@example.com')
    hiring_skills = models.TextField(null=True, blank=True)
    how_heard_about_codeunity = models.CharField(max_length=255, null=True, blank=True)
    # looking_for = models.CharField(max_length=50, choices=[('freelance', 'Freelance Contractor'), ('full_time', 'Full Time Employee')], null=True, blank=True)
    years_of_experience = models.IntegerField(null=True, blank=True)
    LOOKING_FOR_CHOICES = [
        ('freelance', 'Freelance Contractor'),
        ('full_time', 'Full Time Employee')
    ]
    looking_for = models.CharField(max_length=10, choices=LOOKING_FOR_CHOICES, null=True, blank=True)



# class Job(models.Model):
#     company_name = models.CharField(max_length=255)
#     company_twitter = models.CharField(max_length=255, null=True, blank=True)
#     company_email = models.EmailField()
#     invoice_email = models.EmailField()
#     invoice_address = models.TextField()
#     invoice_notes = models.TextField(null=True, blank=True)
#     pay_later = models.BooleanField(default=False)
#     position = models.CharField(max_length=255)
#     tags = models.CharField(max_length=255)
#     primary_tag = models.CharField(max_length=255)
#     location_restriction = models.CharField(max_length=255)
#     annual_salary_min = models.DecimalField(max_digits=10, decimal_places=2)
#     annual_salary_max = models.DecimalField(max_digits=10, decimal_places=2)
#     job_description = models.TextField()
#     apply_url = models.URLField(null=True, blank=True)
#     apply_email_address = models.EmailField(null=True, blank=True)
#     benefits = models.TextField()
#     how_to_apply = models.TextField()
#     feedback = models.TextField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posted_jobs')

# class JobApplication(models.Model):
#     job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
#     applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications')
#     cover_letter = models.TextField(default='')
#     resume = models.FileField(upload_to='applications/resumes/', null=True, blank=True)
#     applied_at = models.DateTimeField(auto_now_add=True)

# class Notification(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     is_read = models.BooleanField(default=False)

# @receiver(post_save, sender=JobApplication)
# def notify_job_hirer(sender, instance, created, **kwargs):
#     if created:
#         Notification.objects.create(
#             user=instance.job.company_name,
#             message=f'{instance.applicant.username} has applied for your job posting: {instance.job.position}'
#         )
