from django.db import models


class WebCrawler(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
