from rest_framework import serializers
from .models import Server, Channel, Message
from account.serializer import AccountSerializer

class ServerSerializer(serializers.ModelSerializer):
    owner = AccountSerializer(read_only=True)
    members = AccountSerializer(many=True, read_only=True)
    channels = serializers.SerializerMethodField()
    
    class Meta:
        model = Server
        fields = ['id', 'name', 'owner', 'category', 'description', 'members', 'channels', 'created_at', 'updated_at']
    
    def get_channels(self, obj):
        channels = obj.channels.all()
        return ChannelSerializer(channels, many=True).data


class ChannelSerializer(serializers.ModelSerializer):
    owner = AccountSerializer(read_only=True)
    messages_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Channel
        fields = ['id', 'name', 'owner', 'topic', 'server', 'messages_count', 'created_at', 'updated_at']
    
    def get_messages_count(self, obj):
        return obj.messages.count()


class MessageSerializer(serializers.ModelSerializer):
    author = AccountSerializer(read_only=True)
    
    class Meta:
        model = Message
        fields = ['id', 'author', 'channel', 'content', 'created_at', 'updated_at']
