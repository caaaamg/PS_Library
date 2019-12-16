from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView
	)
from .models import Game

class GameListView(ListView):
	model = Game
	template_name = 'Library/home.html'
	context_object_name = 'games'
	ordering = ['title']

class GameDetailView(DetailView):
	model = Game


class GameCreateView(LoginRequiredMixin, CreateView):
	model = Game
	fields = ['title', 'platform', 'genre', 'release_date', 'no_players', 'publisher']


	def form_valid(self, form):
		form.instance.library = self.request.user
		return super().form_valid(form)


class GameUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Game
	fields = ['title', 'platform', 'genre', 'release_date', 'no_players', 'publisher']


	def form_valid(self, form):
		form.instance.library = self.request.user
		return super().form_valid(form)

	def test_func(self):
		game = self.get_object()
		if self.request.user == game.library:
			return True
		return False

class GameDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Game
	success_url = '/'

	def test_func(self):
		game = self.get_object()
		if self.request.user == game.library:
			return True
		return False




