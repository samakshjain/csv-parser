from django.db import models


class Data(models.Model):
    reference_id = models.CharField(max_length=16)
    timestamp = models.CharField(max_length=10)
    handle = models.CharField(max_length=64)
    tweet = models.CharField(max_length=140)  # Twitter character limit
