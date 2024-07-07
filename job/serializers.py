

from .models import Job, JobApplication

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class JobApplicationSerializer(serializers.ModelSerializer):
    applicant_name = serializers.SerializerMethodField()
    applicant_email = serializers.SerializerMethodField()
    applicant_phone = serializers.SerializerMethodField()
    class Meta:
        model = JobApplication
        # fields = ['job', 'cover_letter', 'resume']
        fields = ['job', 'cover_letter', 'resume', 'applicant_name', 'applicant_email', 'applicant_phone', 'applied_at']

    def get_applicant_name(self, obj):
        return obj.applicant.get_full_name()

    def get_applicant_email(self, obj):
        return obj.applicant.email

    def get_applicant_phone(self, obj):
        return obj.applicant.phone_number

    def create(self, validated_data):
        job = validated_data.get('job')
        applicant = self.context['request'].user
        cover_letter = validated_data.get('cover_letter')
        resume = validated_data.get('resume')

        job_application = JobApplication.objects.create(
            job=job,
            applicant=applicant,
            # name=applicant.get_full_name(),
            # email=applicant.email,
            # phone=applicant.phone_number,
            cover_letter=cover_letter,
            resume=resume
        )

        # Create a notification for the job hirer
        # job_hirer = job.posted_by
        # Notification.objects.create(
        #     user=job_hirer,
        #     message=f"{applicant.username} applied for {job.position}."
        # )

        return job_application

# class NotificationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Notification
#         fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    applications = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ('posted_by',)

    def get_applications(self, obj):
        user = self.context['request'].user
        if user.is_authenticated and user.account_type == 'job_hirer':
            applications = JobApplication.objects.filter(job=obj)
            return JobApplicationSerializer(applications, many=True).data
        return None
