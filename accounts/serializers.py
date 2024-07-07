from .models import CustomUser
# ,Job, JobApplication, Notification
# 
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate

from rest_framework import serializers
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from jobportal.settings import DEFAULT_FROM_EMAIL

CustomUser = get_user_model()
class JobSeekerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name','password', 'email','username', 'location', 'phone_number', 'technical_skills', 'years_of_experience')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            location=validated_data.get('location', ''),
            phone_number=validated_data.get('phone_number', ''),
            technical_skills=validated_data.get('technical_skills', ''),
            years_of_experience=validated_data.get('years_of_experience', 0),
            account_type='job_seeker'
        )
        return user

class JobHirerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'password', 'phone_number','username',
                      'working_email','hiring_skills', 'how_heard_about_codeunity','looking_for')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            username=validated_data['username'],
            password=validated_data['password'],
            working_email=validated_data['working_email'],
            # email=validated_data['working_email'],  # Use working_email as email
            phone_number=validated_data.get('phone_number', ''),
            hiring_skills=validated_data.get('hiring_skills', ''),
            how_heard_about_codeunity=validated_data.get('how_heard_about_codeunity', ''),
            looking_for=validated_data.get('looking_for', ''),

            account_type='job_hirer'
        )
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'last_name', 'phone_number', 'location', 'technical_skills', 'bio', 
            'account_type', 'country', 'gender', 'website', 'telegram', 'github', 'x', 
            'linkedin', 'instagram', 'spoken_languages', 'available_for_work_from_date', 
            'preferred_annual_pay', 'preferred_hourly_pay', 'resume', 'profile_picture',
            'company_name', 'designation', 'company_description', 'company_stage', 'product_service', 'company_photo','working_email','years_of_experience','email'
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.account_type == 'job_seeker':
            job_seeker_fields = [
                'first_name', 'last_name', 'phone_number', 'email','location', 'technical_skills', 'bio', 
                'account_type', 'country', 'gender', 'website', 'telegram', 'github', 'x', 
                'linkedin', 'instagram', 'spoken_languages', 'available_for_work_from_date', 
                'preferred_annual_pay', 'preferred_hourly_pay', 'resume', 'profile_picture','years_of_experience'
            ]
            return {field: representation[field] for field in job_seeker_fields}
        elif instance.account_type == 'job_hirer':
            job_hirer_fields = [
                'first_name', 'last_name', 'phone_number', 'company_name', 'designation', 
                'company_description', 'company_stage', 'product_service', 'company_photo','working_email'
            ]
            return {field: representation[field] for field in job_hirer_fields}
        return representation

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            user = CustomUser.objects.get(email=value)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")
        return value

    def save(self):
        request = self.context.get('request')
        email = self.validated_data['email']
        user = CustomUser.objects.get(email=email)
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        password_reset_url = f"{request.scheme}://{request.get_host()}/accounts/reset-password/{uid}/{token}/"
        
        # Send password reset email
        send_mail(
            'Password Reset Request',
            f'Please click the link below to reset your password: {password_reset_url}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
