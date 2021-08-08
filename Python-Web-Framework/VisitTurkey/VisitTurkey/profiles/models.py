from django.contrib.auth import get_user_model
from django.db import models

CustomUserModel = get_user_model()


class Profile(models.Model):
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    city = models.CharField(max_length=20, blank=True)

    user = models.OneToOneField(
        CustomUserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    is_complete = models.BooleanField(default=False)
