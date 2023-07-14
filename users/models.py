from django.db import models
from django.contrib.auth.models import AbstractUser


class ExtendedUser(AbstractUser):

    email = models.EmailField()

    # USERNAME_FIELD = ('username',)
    EMAIL_FIELD  = ('email',)
# Create your models here.
