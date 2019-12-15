from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
	title = models.CharField(max_length=100)
	platfrom = models.CharField(max_length=25)
	genre = models.CharField(max_length=25)
	release_Date = models.DateField()
	no_players = models.IntegerField()
	publisher = models.CharField(max_length=100)
	library = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.title




# Create your models here.
