from django.db import models

class accountData(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)

class interestedstockData(models.Model):
    name = models.CharField(max_length=100, null=True)
    group = models.CharField(max_length=50, null=True)
    company1 = models.CharField(max_length=50, null=True)
    company2 = models.CharField(max_length=50, null=True)
    company3 = models.CharField(max_length=50, null=True)
    company4 = models.CharField(max_length=50, null=True)
    company5 = models.CharField(max_length=50, null=True)
    company6 = models.CharField(max_length=50, null=True)
    company7 = models.CharField(max_length=50, null=True)
    company8 = models.CharField(max_length=50, null=True)
    company9 = models.CharField(max_length=50, null=True)
    company10 = models.CharField(max_length=50, null=True)