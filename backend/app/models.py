from django.db import models

class CompanyUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class GeneralUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
