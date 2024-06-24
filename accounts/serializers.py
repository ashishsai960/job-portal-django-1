from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

CustomUser = get_user_model()

class JobSeekerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'password', 'email', 'location', 'phone_number')
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
            account_type='job_seeker'
        )
        return user

class JobHirerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'password', 'working_email', 'phone_number', 'location', 'company_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            username=validated_data['username'],
            password=validated_data['password'],
            working_email=validated_data['email'],
            phone_number=validated_data.get('phone_number', ''),
            location=validated_data.get('location', ''),
            company_name=validated_data.get('company_name', ''),
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
            'company_name', 'designation', 'company_description', 'company_stage', 'product_service', 'company_photo','working_email'
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.account_type == 'job_seeker':
            job_seeker_fields = [
                'first_name', 'last_name', 'phone_number', 'location', 'technical_skills', 'bio', 
                'account_type', 'country', 'gender', 'website', 'telegram', 'github', 'x', 
                'linkedin', 'instagram', 'spoken_languages', 'available_for_work_from_date', 
                'preferred_annual_pay', 'preferred_hourly_pay', 'resume', 'profile_picture'
            ]
            return {field: representation[field] for field in job_seeker_fields}
        elif instance.account_type == 'job_hirer':
            job_hirer_fields = [
                'first_name', 'last_name', 'working_email', 'phone_number', 'company_name', 'designation', 
                'company_description', 'company_stage', 'product_service', 'company_photo'
            ]
            return {field: representation[field] for field in job_hirer_fields}
        return representation

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
