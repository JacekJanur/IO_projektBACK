from django.test import TestCase
from .models import User
from django.test import Client
import json
from django.contrib.auth.hashers import make_password

c = Client()

class UserViewTest(TestCase):
	def test_register_view(self):
		"""Checking /register view"""
		response = c.post('/users/register', {'name': 'fred', 'passwd': 'secret'})
		self.assertJSONEqual(
			str(response.content, encoding='utf8'),
			{'status':405,'message':"bad data"}
		)

		response = c.post('/users/register', {'name': 'fred', 'password': 'secret', 'email': 'fred@wp.pl'})
		response = json.loads(response.content.decode('utf-8'))
		self.assertEqual(response['status'], 200)

		response = c.post('/users/register', {'name': 'fred', 'password': 'secret', 'email': 'fred@wp.pl'})
		self.assertJSONEqual(
			str(response.content, encoding='utf8'),
			{'status':405,'message':"Email exist"}
		)

	def test_login_view(self):
		"""Checking /register view"""

		fred = User.objects.create(name="fred", email="fred@wp.pl", password=make_password('secret'))

		response = c.post('/users/login', {'name': 'fred', 'passwd': 'secret'})
		self.assertJSONEqual(
			str(response.content, encoding='utf8'),
			{'message':"bad data"}
		)

		response = c.post('/users/login', {'email': 'fred', 'password': 'secret'})
		self.assertJSONEqual(
			str(response.content, encoding='utf8'),
			{'message': "no user with this email"}
		)

		response = c.post('/users/login', {'email': 'fred@wp.pl', 'password': 'secret123'})
		self.assertJSONEqual(
			str(response.content, encoding='utf8'),
			{'message': "wrong password"}
		)

		response = c.post('/users/login', {'email': 'fred@wp.pl', 'password': 'secret'})
		response = json.loads(response.content.decode('utf-8'))
		self.assertIn( 'token' , response)


