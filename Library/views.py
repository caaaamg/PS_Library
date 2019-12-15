from django.shortcuts import render
from django.views.generic import ListView
from .models import Game

def home(request):
	context = {
		'games' : Game.objects.all()
	} 
	return render(request, 'Library/home.html', context)

class GameListView(ListView):
	model = Game
	template_name = 'Library/home.html'
	context_object_name = 'games'