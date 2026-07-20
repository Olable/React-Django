from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Server, Channel, Message
from .serializer import ServerSerializer, ChannelSerializer, MessageSerializer

class ServerListViewSet(viewsets.ViewSet):
    """ViewSet for Server CRUD operations with filtering"""
    
    queryset = Server.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """List all servers, optionally filtered by category"""
        queryset = self.queryset.all()
        category = request.query_params.get('category')

        if category:
            queryset = queryset.filter(category=category)

        serializer = ServerSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Create a new server (authenticated user becomes owner)"""
        serializer = ServerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        """Get a single server by ID"""
        try:
            server = self.queryset.get(pk=pk)
        except Server.DoesNotExist:
            return Response({"detail": "Server not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ServerSerializer(server)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        """Update a server (owner only)"""
        try:
            server = self.queryset.get(pk=pk)
        except Server.DoesNotExist:
            return Response({"detail": "Server not found."}, status=status.HTTP_404_NOT_FOUND)
        
        if server.owner != request.user:
            return Response({"detail": "Only the owner can update this server."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = ServerSerializer(server, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        """Delete a server (owner only)"""
        try:
            server = self.queryset.get(pk=pk)
        except Server.DoesNotExist:
            return Response({"detail": "Server not found."}, status=status.HTTP_404_NOT_FOUND)
        
        if server.owner != request.user:
            return Response({"detail": "Only the owner can delete this server."}, status=status.HTTP_403_FORBIDDEN)
        
        server.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['get'])
    def channels(self, request, pk=None):
        """Get all channels for a server"""
        try:
            server = self.queryset.get(pk=pk)
        except Server.DoesNotExist:
            return Response({"detail": "Server not found."}, status=status.HTTP_404_NOT_FOUND)
        
        channels = server.channels.all()
        serializer = ChannelSerializer(channels, many=True)
        return Response(serializer.data)


class ChannelViewSet(viewsets.ViewSet):
    """ViewSet for Channel CRUD operations"""
    
    queryset = Channel.objects.all()
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        """List all channels, optionally filtered by server"""
        queryset = self.queryset.all()
        server = request.query_params.get('server')
        
        if server:
            queryset = queryset.filter(server=server)
        
        serializer = ChannelSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Create a new channel"""
        serializer = ChannelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        """Get a single channel by ID"""
        try:
            channel = self.queryset.get(pk=pk)
        except Channel.DoesNotExist:
            return Response({"detail": "Channel not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ChannelSerializer(channel)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        """Update a channel (owner only)"""
        try:
            channel = self.queryset.get(pk=pk)
        except Channel.DoesNotExist:
            return Response({"detail": "Channel not found."}, status=status.HTTP_404_NOT_FOUND)
        
        if channel.owner != request.user:
            return Response({"detail": "Only the owner can update this channel."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = ChannelSerializer(channel, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        """Delete a channel (owner only)"""
        try:
            channel = self.queryset.get(pk=pk)
        except Channel.DoesNotExist:
            return Response({"detail": "Channel not found."}, status=status.HTTP_404_NOT_FOUND)
        
        if channel.owner != request.user:
            return Response({"detail": "Only the owner can delete this channel."}, status=status.HTTP_403_FORBIDDEN)
        
        channel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['get'])
    def messages(self, request, pk=None):
        """Get all messages for a channel"""
        try:
            channel = self.queryset.get(pk=pk)
        except Channel.DoesNotExist:
            return Response({"detail": "Channel not found."}, status=status.HTTP_404_NOT_FOUND)
        
        messages = channel.messages.all().order_by('created_at')
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)


class MessageViewSet(viewsets.ViewSet):
    """ViewSet for Message CRUD operations"""
    
    queryset = Message.objects.all()
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        """List all messages, optionally filtered by channel"""
        queryset = self.queryset.all()
        channel = request.query_params.get('channel')
        
        if channel:
            queryset = queryset.filter(channel=channel)
        
        serializer = MessageSerializer(queryset.order_by('created_at'), many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Create a new message"""
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        """Get a single message by ID"""
        try:
            message = self.queryset.get(pk=pk)
        except Message.DoesNotExist:
            return Response({"detail": "Message not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MessageSerializer(message)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        """Update a message (author only)"""
        try:
            message = self.queryset.get(pk=pk)
        except Message.DoesNotExist:
            return Response({"detail": "Message not found."}, status=status.HTTP_404_NOT_FOUND)
        
        if message.author != request.user:
            return Response({"detail": "Only the author can update this message."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = MessageSerializer(message, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        """Delete a message (author only)"""
        try:
            message = self.queryset.get(pk=pk)
        except Message.DoesNotExist:
            return Response({"detail": "Message not found."}, status=status.HTTP_404_NOT_FOUND)
        
        if message.author != request.user:
            return Response({"detail": "Only the author can delete this message."}, status=status.HTTP_403_FORBIDDEN)
        
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
