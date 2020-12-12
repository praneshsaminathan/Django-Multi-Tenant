from django.db import models


# Create your models here.
class MyUser(models.Model):
    name = models.CharField(max_length=100)


class Tempoo(models.Model):
    name = models.CharField(max_length=100)