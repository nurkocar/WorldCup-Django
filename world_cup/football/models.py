from django.db import models
from django import forms

# Create your models here.
        
class Country(models.Model):
    country_name = models.CharField(max_length=40)
    fifa_ranking = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Countries'
    def ___str__(self):
        return str(self.country_name)

class Player(models.Model):
    player_name = models.CharField(max_length=40)
    player_team = models.ForeignKey('Country', on_delete=models.CASCADE, blank=True, null=True)
    age = models.PositiveIntegerField()
    def ___str__(self):
        return str(self.player_name)
