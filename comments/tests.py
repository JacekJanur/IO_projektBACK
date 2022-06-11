from django.test import TestCase
from users.models import User
from django.test import Client
from games.models import Game
from genres.models import Genre
from .models import Comment
import json

c = Client()

class CommentTest(TestCase):
	def setUp(self):
		g = Genre.objects.create(name="jrpg")
		Game.objects.create(name="firstG", description="desc", genre=g)
		Game.objects.create(name="secondG", description="desc", genre=g)
		User.objects.create(name="User1", email="u1@wp.pl", password="secret", token="123")

	def test_create_ok(self):
		gam = Game.objects.get(name="firstG")
		response = c.post('/comments/add', {'game': gam.id, 'token': '123', 'text': "tekst"})
		self.assertEqual(response.status_code, 200)

	def test_create_bad_token(self):
		gam = Game.objects.get(name="firstG")
		response = c.post('/comments/add', {'game': gam.id, 'token': '12', 'text': "tekst"})
		self.assertEqual(response.status_code, 401)

	def test_create_bad_data(self):
		gam = Game.objects.get(name="firstG")
		response = c.post('/comments/add', {'gam5e': gam.id, 'token': '12', 'text': "tekst"})
		self.assertEqual(response.status_code, 401)

	def test_create_bad_game(self):
		gam = Game.objects.get(name="firstG")
		response = c.post('/comments/add', {'gam5e': 5, 'token': '12', 'text': "tekst"})
		self.assertEqual(response.status_code, 401)