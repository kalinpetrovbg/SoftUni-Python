from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='profiles')

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        name='id',
    )

