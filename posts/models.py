from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Post(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete = models.CASCADE ,default=1)
    date_created = models.DateTimeField(auto_now=True,auto_now_add=False)
    date_updated = models.DateTimeField(auto_now=False,auto_now_add=True)


    def __str__(self):
        return self.name

