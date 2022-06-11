from django.test import TestCase
from .models import Genre
import json

class ReviewTest(TestCase):
	def setUp(self):
		g = Genre.objects.create(name="jrpg")

	def test_create_ok(self):
		gen = Genre.objects.get(name="jrpg")
		self.assertEqual(gen.name, "jrpg")