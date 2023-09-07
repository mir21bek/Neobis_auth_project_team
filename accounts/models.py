from django.db import models

from authemail.models import EmailUserManager, EmailAbstractUser


class UserProfile(EmailAbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = EmailUserManager()

    def __str__(self):
        return self.email
