from django.test import TestCase
from .models import File

class FileModelTest(TestCase):
    def test_file_fields(self):
        # Create a sample file
        file = File.objects.create(
            file='home/acer/Downloads/mountains.jpg',
            format='jpg',
            name='Test File',
            ordering=1
        )

        # Assert the file fields
        self.assertEqual(file.file, 'home/acer/Downloads/mountains.jpg')
        self.assertEqual(file.format, 'jpg')
        self.assertEqual(file.name, 'Test File')
        self.assertEqual(file.ordering, 1)
