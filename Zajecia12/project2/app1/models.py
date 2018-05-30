from django.db import models

class Person(models.Model):
    im = models.CharField(max_length=30)
    naz = models.CharField(max_length=30)
