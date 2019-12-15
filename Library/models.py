from django.db import models
from django.contrib.auth.models import User



class Game(models.Model):
	g_name = models.CharField(max_length=100)
	g_platfrom = models.CharField(max_length=25)
	g_genre = models.CharField(max_length=25)
	g_release_date = models.DateField()
	g_no_players = models.IntegerField()
	g_publisher = models.CharField(max_length=100)

	def __str__(self):
		return self.g_name



# Create your models here.
