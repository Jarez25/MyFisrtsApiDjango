from django.db import models

# Create your models here.

class Progamador(models.Model):
    full_name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    ia_active = models.BooleanField(default=True)
