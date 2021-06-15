from django.db import models

class accountData(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)

class interestedstockData(models.Model):
    name = models.CharField(max_length=100, null=True)
    group = models.CharField(max_length=50, default="")
    company1 = models.CharField(max_length=50, default="")
    company2 = models.CharField(max_length=50, default="")
    company3 = models.CharField(max_length=50, default="")
    company4 = models.CharField(max_length=50, default="")
    company5 = models.CharField(max_length=50, default="")
    company6 = models.CharField(max_length=50, default="")
    company7 = models.CharField(max_length=50, default="")
    company8 = models.CharField(max_length=50, default="")
    company9 = models.CharField(max_length=50, default="")
    company10 = models.CharField(max_length=50, default="")