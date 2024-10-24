from django.db import models

# Create your models here.

class PlayerPosition(models.Model):
    pass



class Player(models.Model):
    name = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255)
    shirt_number = models.IntegerField()

    # relacao com player position
