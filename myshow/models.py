from django.db import models

# Create your models here.

class user(models.Model):
    name = models.TextField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    password = models.TextField(max_length=100)

    def __str__(self):
        return self.name