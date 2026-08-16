from rest_framework import viewsets
from rest_framework.response import Response

from .models import Server
from .serializer import ServerSerializer


class ServerListViewSet(viewsets.ViewSet):
    queryset = Server.objects.all()

    def list(self, request):
        queryset = Server.objects.all()

        category = request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__name=category)

        serializer = ServerSerializer(queryset, many=True)
        return Response(serializer.data)