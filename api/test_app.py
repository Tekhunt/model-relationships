from django.test import TestCase
from .models import Items


class PostTestCase(TestCase):
    def testPost(self):
        items = Items(name="My Title")
        self.assertEqual(items.name, "My Title")
