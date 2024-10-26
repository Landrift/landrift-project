from rest_framework import viewsets
from .models import CompanyUser, GeneralUser
from .serializers import CompanyUserSerializer, GeneralUserSerializer

class CompanyUserViewSet(viewsets.ModelViewSet):
    queryset = CompanyUser.objects.all()
    serializer_class = CompanyUserSerializer

class GeneralUserViewSet(viewsets.ModelViewSet):
    queryset = GeneralUser.objects.all()
    serializer_class = GeneralUserSerializer
