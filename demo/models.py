from django.db import models
from django.views import generic
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns

#class WebCrawler(models.Model):
#    title = models.CharField(max_length=200)
#    url = models.URLField(max_length=200)
#
#    def __str__(self):
#        return '{}'.format(self.title)
#
#class WebList(generic.ListView):
#    weblist = WebCrawler

class WebLinks(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title