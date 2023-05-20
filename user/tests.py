from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserModelTest(TestCase):
    def test_user_fields(self):
        # Create a sample user
        user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            phone_number='123456789',
            middle_name='Test Middle',
            is_verified=True
        )

        # Check the user fields
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('testpassword'))
        self.assertEqual(user.phone_number, '123456789')
        self.assertEqual(user.middle_name, 'Test Middle')
        self.assertTrue(user.is_verified)

    def test_user_creation(self):
        # Create a sample user
        user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            phone_number='123456789',
            middle_name='Test Middle',
            is_verified=True
        )

        # Check user creation
        self.assertIsNotNone(user)
        self.assertIsInstance(user, User)
