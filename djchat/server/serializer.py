from rest_framework import serializers

from .models import Category, Server

class ServerSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Category.objects.all()
    )

    class Meta:
        model = Server
        fields = '__all__'