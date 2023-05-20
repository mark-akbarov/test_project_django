from decimal import Decimal
from django.test import TestCase
from .models import Product, File


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a File instance for testing
        file = File.objects.create(file='home/acer/Downloads/mountains.jpg', name='Test File')

        # Create a Product instance for testing
        Product.objects.create(name='Test Product', price=Decimal(10.99), description='Test Description', image=file)

    def test_product_fields(self):
        product = Product.objects.get(id=1)

        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.price, Decimal('10.99'))
        self.assertEqual(product.description, 'Test Description')

    def test_product_image(self):
        product = Product.objects.get(id=1)
        file = product.image

        self.assertEqual(file.file, 'home/acer/Downloads/mountains.jpg')
        self.assertEqual(file.name, 'Test File')
        self.assertEqual(file.format, 'jpg')
        self.assertEqual(file.ordering, 1)
