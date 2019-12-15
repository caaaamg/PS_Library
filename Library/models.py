from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
	Title = models.CharField(max_length=100)
	Platfrom = models.CharField(max_length=25)
	Genre = models.CharField(max_length=25)
	Release_Date = models.DateField()
	No_Players = models.IntegerField()
	Publisher = models.CharField(max_length=100)

	def __str__(self):
		return self.Title


class Library(models.Model):
	games = models.ManyToManyField(Game)
	Owner = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		return f'{self.Owner.username}\'s Library'


# Create your models here.
