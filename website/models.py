from django.db import models
from django.utils.timezone import now

# Create your models here.


class Contact(models.Model):
    name = models.CharField(
        max_length=255,
    )
    subject = models.CharField(
        max_length=255,
    )
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name+': '+self.email


class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
