from rest_framework import serializers
from .models import Job 

from .models import Document

class JobRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

    def create(self, validated_data):
        job = Job.objects.create(**validated_data)
        return job



class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['profile_pic', 'resume', 'cover_letter']
        
