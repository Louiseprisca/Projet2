from django.db import models

# Create your models here.

class Feature(models.Model):
    name = models.CharField(max_length=50, default='')
    details = models.CharField(max_length=255, default='')