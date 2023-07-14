from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now=True,auto_now_add=False)
    date_update = models.DateTimeField(auto_now=False,auto_now_add=True)


    def __str__(self):
        return self.name

