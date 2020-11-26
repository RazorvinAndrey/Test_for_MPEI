from django.db import models

# Create your models here.



class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

class Voice(models.Model):
    text = models.CharField(max_length=500)
    num = models.IntegerField(default=0)


