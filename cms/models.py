from django.db import models

# Create your models here.

class Pages(models.Model):
    name = models.CharField(max_length=32)
    page = models.TextField()
    def __str__(self):
        return self.name

class Titular(models.Model):
    name = models.CharField(max_length=32)
    html = models.TextField()
    def __str__(self):
        return self.name
