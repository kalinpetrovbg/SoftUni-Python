from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=30)
    type = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='media_files',)


