from django.test import TestCase
from users.models import User
from django.test import Client
from games.models import Game
from genres.models import Genre
import json

c = Client()

class ReviewTest(TestCase):
	def setUp(self):
		g = Genre.objects.create(name="jrpg")
		Game.objects.create(name="firstG", description="desc", genre=g)
		Game.objects.create(name="secondG", description="desc", genre=g)
		User.objects.create(name="User1", email="u1@wp.pl", password="secret", token="123")

	def test_create_ok(self):
		gam = Game.objects.get(name="firstG")
		response = c.post('/reviews/add', {'game': gam.id, 'token': '123', 'review': 1})
		self.assertEqual(response.status_code, 200)

	def test_create_bad_data(self):
		gam = Game.objects.get(name="firstG")
		response = c.post('/reviews/add', {'game2': gam.id, 'token': '123', 'review': 1})
		self.assertEqual(response.status_code, 401)

	def test_create_bad_token(self):
		gam = Game.objects.get(name="firstG")
		response = c.post('/reviews/add', {'game': gam.id, 'token': '12', 'review': 1})
		self.assertEqual(response.status_code, 401)

	def test_create_bad_number(self):
		gam = Game.objects.get(name="firstG")
		response = c.post('/reviews/add', {'game': gam.id, 'token': '12', 'review': "asd"})
		self.assertEqual(response.status_code, 401)

	def test_create_too_big_number(self):
		gam = Game.objects.get(name="firstG")
		response = c.post('/reviews/add', {'game': gam.id, 'token': '12', 'review': 7})
		self.assertEqual(response.status_code, 401)

	def test_create_too_small_number(self):
		gam = Game.objects.get(name="firstG")
		response = c.post('/reviews/add', {'game': gam.id, 'token': '12', 'review': -1})
		self.assertEqual(response.status_code, 401)
