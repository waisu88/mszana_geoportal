from django.db import models

# Create yor models here.
class Sample(models.Model):
    attachment = models.FileField()