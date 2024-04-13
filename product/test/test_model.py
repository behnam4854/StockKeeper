from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from product.models import Product


class PublicModelTests(TestCase):
    """For testing public test like model creation"""

    def setUp(self):
        self.client = APIClient()

    def test_my_model_str(self):
        product = Product.objects.create(name="test product", description = 'no description', quantity=2)
        self.assertEqual(str(product), "test product")