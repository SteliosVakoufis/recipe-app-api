"""
Views for the user API.
"""

from rest_framework import generics

from . import serializers as user_serializers


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = user_serializers.UserSerializer
