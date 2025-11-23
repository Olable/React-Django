from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Server(models.Model):
    
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_servers')
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='server_category')
    description = models.CharField(blank=True, null=True, max_length=255)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='servers', blank=True)  
        
        
    def __str__(self):
        return self.name 


class Channel(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='channel_servers')
    topic = models.CharField(max_length=100)
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name='channels')
    
    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Channel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name 