from django.db import models
from django.views import generic
from django.utils import timezone
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns

class Category(models.Model):
    type = models.CharField(max_length=30)
    def __str__(self):
        return self.type

class Datacrawl(models.Model):
    type = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.CharField(max_length=280)
    username = models.CharField(max_length=100)
    url = models.CharField(max_length=250)
    created = models.DateTimeField()
    added = models.DateTimeField(editable=False)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.id:
            self.added = timezone.now()
        super().save(*args, **kwargs)