from django.db import models

# Create your models here.

class Villager(models.Model):
    name = models.CharField(max_length=20)
    personality = models.TextField()
    birthday = models.CharField(max_length=40, default='01/01')

    def __str__(self):
        """TEST"""
        return self.name