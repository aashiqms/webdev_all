from django.db import models
from django import forms


class User(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=264, unique=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "User"


class Product(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name_optional = models.CharField(max_length=120, blank=True, null=True)
    email_optional = models.EmailField(blank=True, null=True)
    feedback = models.TextField()

    def __str__(self):
        return "{}, {}, {}".format(self.name_optional, self.email_optional, self.feedback)

