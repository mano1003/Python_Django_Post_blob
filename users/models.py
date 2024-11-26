from django.db import models

# Create your models here.
class User(models.Model):
    name: models.EmailField
    password: models.TextField
    age: models.IntegerField

    def __str__(self):
        return self.name
