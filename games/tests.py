from django.test import TestCase
from .models import Game
from genres.models import Genre
from django.test import Client

c = Client()

class GameViewTest(TestCase):
	def setUp(self):
		g = Genre.objects.create(name="jrpg")
		Game.objects.create(name="firstG", description="desc", genre=g)
		Game.objects.create(name="secondG", description="desc", genre=g)

	def test_index_view(self):
		"""Checking /games view"""
		response = c.get('/games/')
		self.assertEqual(len(response.data), 2)

	def test_detail_view(self):
		"""Checking /games view"""
		gam = Game.objects.get(name="firstG")
		response = c.get('/games/'+str(gam.pk), follow=True)
		self.assertEqual(response.data['name'], "firstG")
		self.assertEqual(response.data['description'], "desc")
