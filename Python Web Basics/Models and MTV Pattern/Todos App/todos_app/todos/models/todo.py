from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id}: {self.name}"

    class Meta:
        verbose_name_plural = 'people'

class Todo(models.Model):
    name_of_task = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    person_test = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(max_length=30, blank=True, null=True)
    owner = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        null=True
    )

class Category(models.Model):
    WORK_CHOICE = 'Work'
    HOME_CHOICE = 'Home'
    MY_CHOICES = (
        (WORK_CHOICE, 'Work things'),
        (HOME_CHOICE, 'Home things')
    )
    name = models.CharField(max_length=20, choices=MY_CHOICES)

    class Meta:
        verbose_name_plural = 'categories'
