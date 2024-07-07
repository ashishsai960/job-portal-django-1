# from django.db import models
# import datetime
# from django.contrib.auth.models import User
# from django.conf import settings


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
#     created_at = models.DateTimeField(default=datetime.datetime.now)
#     updated_at = models.DateTimeField(default=datetime.datetime.now)

#     def __str__(self):
#         return self.position
 
    
  
# class Document(models.Model):
    
#     profile_pic = models.ImageField(upload_to='profile_pics/')
#     resume = models.FileField(upload_to='resumes/')
#     cover_letter = models.FileField(upload_to='cover_letters/')

#     def __str__(self):
#         return f"{self.user.username}'s documents"
# class Profile(models.Model):
#     profile_pic =models.ImageField(null=True, blank=True)
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)



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


from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from django.conf import settings

class Job(models.Model):
    company_name = models.CharField(max_length=255)
    company_twitter = models.CharField(max_length=255, null=True, blank=True)
    company_email = models.EmailField()
    invoice_email = models.EmailField()
    invoice_address = models.TextField()
    invoice_notes = models.TextField(null=True, blank=True)
    pay_later = models.BooleanField(default=False)
    position = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    primary_tag = models.CharField(max_length=255)
    location_restriction = models.CharField(max_length=255)
    annual_salary_min = models.DecimalField(max_digits=10, decimal_places=2)
    annual_salary_max = models.DecimalField(max_digits=10, decimal_places=2)
    job_description = models.TextField()
    apply_url = models.URLField(null=True, blank=True)
    apply_email_address = models.EmailField(null=True, blank=True)
    benefits = models.TextField()
    how_to_apply = models.TextField()
    feedback = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posted_jobs',default=1)

class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications')
    cover_letter = models.TextField(default='')
    resume = models.FileField(upload_to='applications/resumes/', null=True, blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)

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
