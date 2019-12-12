from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


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
        serializer = self.serializer_class(date=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)
