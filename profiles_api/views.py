from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permission

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle createing and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permission.UpdateOwnProfile,)


class HelloViewSet(viewsets.ViewSet):
    """Test API with View Sets"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a Hello message"""
        a_viewset = [
            "Create View Sets(List)",
            "Is similar to a django view",
            "Gives you the most control over you application logic",
            "Mapped URL with Router"
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView feature"""

        an_apiview = [
            "Uses HTTP Method as function (get , post, patch, put , delete)",
            "Is similar to a django view",
            "Gives you the most control over you application logic",
            "Is mapped manually to URLs"
        ]

        return Response({'message': 'Hello!!!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create Hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Put Method"""
        return Response({'message': 'PUT'})
