from __future__ import unicode_literals

from django.db import models

# Create your models here.
class users(models.Model):
    full_name=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
