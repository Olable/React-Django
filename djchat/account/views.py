from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import Account
from .serializer import AccountSerializer, SignupSerializer, LoginSerializer


class SignupView(APIView):
    """User signup endpoint"""
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Generate tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': AccountSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """User login endpoint"""
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            
            user = authenticate(username=username, password=password)
            if user is not None:
                # Generate tokens
                refresh = RefreshToken.for_user(user)
                return Response({
                    'user': AccountSerializer(user).data,
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountViewSet(viewsets.ViewSet):
    """ViewSet for Account operations"""
    permission_classes = [IsAuthenticated]
    
    def retrieve(self, request, pk=None):
        """Get user profile"""
        try:
            user = Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AccountSerializer(user)
        return Response(serializer.data)
    
    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def me(self, request):
        """Get current user profile"""
        serializer = AccountSerializer(request.user)
        return Response(serializer.data)
