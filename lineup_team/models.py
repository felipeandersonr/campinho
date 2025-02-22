from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=255)
    transfermarkt_image_url = models.CharField(max_length=255)
    transfermarkt_url = models.CharField(max_length=255, unique=True)


class Player(models.Model):
    name = models.CharField(max_length=255)
    shirt_number = models.CharField(max_length=4)
    transfermarkt_url = models.CharField(max_length=255)

    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="players")
