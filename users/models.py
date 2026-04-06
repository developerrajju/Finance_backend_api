from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
        ('viewer', 'Viewer'),
        ('analyst', 'Analyst'),
        ('admin', 'Admin'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='viewer')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username
    
from django.db import models

