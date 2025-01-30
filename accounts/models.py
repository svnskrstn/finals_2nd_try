from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    role = models.CharField(max_length=20,
        choices=[
            ('User', 'User'),
            ('Artist', 'Artist'),
        ],
        default='User'
    )

    bio = models.TextField()
    image = models.ImageField(upload_to='artists/', default='profile_image/default.png')