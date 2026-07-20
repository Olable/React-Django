from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from server.models import Server, Channel, Message, Category
from account.models import Account

User = get_user_model()

class ServerViewTests(TestCase):
    """Tests for Server endpoints"""
    
    def setUp(self):
        self.client = APIClient()
        self.user = Account.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.other_user = Account.objects.create_user(
            username='otheruser',
            email='other@example.com',
            password='testpass123'
        )
        self.category = Category.objects.create(
            name='Gaming',
            description='Gaming servers'
        )
        self.server = Server.objects.create(
            name='Test Server',
            owner=self.user,
            category=self.category,
            description='A test server'
        )
        
        # Get JWT token
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
    
    def test_list_servers(self):
        """Test listing servers"""
        response = self.client.get('/api/server/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_create_server(self):
        """Test creating a server"""
        data = {
            'name': 'New Server',
            'category': self.category.id,
            'description': 'A new server'
        }
        response = self.client.post('/api/server/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['owner']['username'], 'testuser')
    
    def test_retrieve_server(self):
        """Test retrieving a single server"""
        response = self.client.get(f'/api/server/{self.server.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Server')
    
    def test_update_server_owner(self):
        """Test updating server as owner"""
        data = {'description': 'Updated description'}
        response = self.client.patch(f'/api/server/{self.server.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], 'Updated description')
    
    def test_update_server_not_owner(self):
        """Test updating server as non-owner"""
        # Switch to other user
        refresh = RefreshToken.for_user(self.other_user)
        access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        
        data = {'description': 'Updated description'}
        response = self.client.patch(f'/api/server/{self.server.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_delete_server_owner(self):
        """Test deleting server as owner"""
        response = self.client.delete(f'/api/server/{self.server.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Server.objects.filter(id=self.server.id).exists())
    
    def test_get_server_channels(self):
        """Test getting channels for a server"""
        channel = Channel.objects.create(
            name='general',
            owner=self.user,
            server=self.server
        )
        response = self.client.get(f'/api/server/{self.server.id}/channels/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class ChannelViewTests(TestCase):
    """Tests for Channel endpoints"""
    
    def setUp(self):
        self.client = APIClient()
        self.user = Account.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.category = Category.objects.create(name='Gaming')
        self.server = Server.objects.create(
            name='Test Server',
            owner=self.user,
            category=self.category
        )
        self.channel = Channel.objects.create(
            name='General',
            owner=self.user,
            server=self.server
        )
        
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
    
    def test_list_channels(self):
        """Test listing channels"""
        response = self.client.get('/api/channel/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_create_channel(self):
        """Test creating a channel"""
        data = {
            'name': 'announcements',
            'server': self.server.id,
            'topic': 'Important announcements'
        }
        response = self.client.post('/api/channel/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'announcements')
    
    def test_channel_name_lowercase(self):
        """Test that channel names are converted to lowercase"""
        data = {
            'name': 'TestChannel',
            'server': self.server.id
        }
        response = self.client.post('/api/channel/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'testchannel')


class MessageViewTests(TestCase):
    """Tests for Message endpoints"""
    
    def setUp(self):
        self.client = APIClient()
        self.user = Account.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.category = Category.objects.create(name='Gaming')
        self.server = Server.objects.create(
            name='Test Server',
            owner=self.user,
            category=self.category
        )
        self.channel = Channel.objects.create(
            name='general',
            owner=self.user,
            server=self.server
        )
        self.message = Message.objects.create(
            author=self.user,
            channel=self.channel,
            content='Test message'
        )
        
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
    
    def test_list_messages(self):
        """Test listing messages"""
        response = self.client.get('/api/message/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_create_message(self):
        """Test creating a message"""
        data = {
            'channel': self.channel.id,
            'content': 'Hello, world!'
        }
        response = self.client.post('/api/message/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['content'], 'Hello, world!')
        self.assertEqual(response.data['author']['username'], 'testuser')
    
    def test_get_channel_messages(self):
        """Test getting messages for a channel"""
        response = self.client.get(f'/api/channel/{self.channel.id}/messages/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['content'], 'Test message')
