from django.shortcuts import render
from rest_framework import viewsets 

class ServerListViewSet(viewsets.ViewSet):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    def list(self, request):
        category = request.query_params.get('category', None)   
        return render(request, 'server_list.html')

