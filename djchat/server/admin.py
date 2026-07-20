from django.contrib import admin
from .models import Server, Channel, Message, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'owner__username')
    ordering = ('-created_at',)

@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'server', 'created_at')
    list_filter = ('server', 'created_at')
    search_fields = ('name', 'owner__username', 'server__name')
    ordering = ('-created_at',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('author', 'channel', 'content', 'created_at')
    list_filter = ('channel', 'created_at')
    search_fields = ('author__username', 'channel__name', 'content')
    ordering = ('-created_at',)
