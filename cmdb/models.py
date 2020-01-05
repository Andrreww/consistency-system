from django.db import models

# Create your models here.

class User(models.Model):
  username = models.CharField(max_length=32)
  password = models.CharField(max_length=32)
class Infss(models.Model):
  trans = models.CharField(max_length=32)
  ids = models.CharField(max_length=32)
  score = models.CharField(max_length=32)
  timenows = models.DateTimeField(auto_now_add=True)
  ptime = models.CharField(max_length=32)
  psco = models.CharField(max_length=32)
  remarks = models.CharField(max_length=300)
