from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Place(models.Model):
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='media_files')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
