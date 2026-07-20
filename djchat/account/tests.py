from django.test import TestCase
from django.contrib.auth import get_user_model
from account.models import Account

User = get_user_model()

class AccountModelTests(TestCase):
    """Tests for Account model"""
    
    def setUp(self):
        self.user = Account.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    
    def test_create_user(self):
        """Test user creation"""
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertTrue(self.user.check_password('testpass123'))
    
    def test_user_str(self):
        """Test user string representation"""
        self.assertEqual(str(self.user), 'testuser')
    
    def test_user_bio(self):
        """Test user bio field"""
        self.user.bio = 'Test bio'
        self.user.save()
        self.assertEqual(self.user.bio, 'Test bio')
