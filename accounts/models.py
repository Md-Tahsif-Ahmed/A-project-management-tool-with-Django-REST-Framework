from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        swappable = 'AUTH_USER_MODEL'  # Ensures Django uses the custom model


    def __str__(self):
        return self.username

