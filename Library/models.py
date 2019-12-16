from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image


class Game(models.Model):
	title = models.CharField(max_length=100)
	platform = models.CharField(max_length=25)
	genre = models.CharField(max_length=25)
	release_date = models.DateField()
	no_players = models.IntegerField()
	publisher = models.CharField(max_length=100)
	box_art = models.ImageField(default='default.jpg', upload_to='box_art')
	library = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('game-detail', kwargs={'pk': self.pk})

	def save(self):
		super().save()

		img = Image.open(self.box_art.path)

		if img.height > 600 and img.width > 600:
			output_size = (400,400)
			img.thumbnail(output_size)
			img.save(self.box_art.path)
