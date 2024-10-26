from rest_framework import serializers
from .models import CompanyUser, GeneralUser

class CompanyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyUser
        fields = '__all__'

class GeneralUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralUser
        fields = '__all__'
