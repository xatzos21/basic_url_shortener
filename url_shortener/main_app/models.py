from django.db import models


class Url(models.Model):
    url = models.CharField(max_length=250)
    slug = models.CharField(max_length=15)
