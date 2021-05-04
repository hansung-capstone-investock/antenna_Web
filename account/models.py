from django.db import models

class accountData(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)