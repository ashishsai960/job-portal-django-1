from django.contrib.auth.models import AbstractUser
from django.db import models

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
