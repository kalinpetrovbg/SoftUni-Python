from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Place(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=30)
    type = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='media_files')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
