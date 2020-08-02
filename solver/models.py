from django.db import models

# Create your models here.
class Solver(models.Model):
    letters = models.CharField(max_length=100)
    size = models.PositiveSmallIntegerField()