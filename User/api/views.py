from User.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from User.api.serializers import RegistrationSerializer

@api_view(['POST',])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            User = serializer.save()
            data['response'] = "successfully registered a new user"
            data['email'] = User.email
            data['username'] = User.username
        else:
            data = serializer.errors
        return Response(data)
