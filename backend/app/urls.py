from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'company', views.CompanyUserViewSet)
router.register(r'user', views.GeneralUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
