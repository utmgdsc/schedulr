import os

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import NoteSerializer
from base.models import Note
from base.models import Tcourse
from .serializers import TcourseSerializer
from .calculateCal import generate_events
# import mock_data.csv
import csv

from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        
        
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getRoute(request):
    
    routes = [
        '/api/token',
        '/api/token/refresh',
        'api/notes',
        'api/register',
        'api/events',
    ]
    
    return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    
    user = request.user
    
    notes = user.note_set.all()
    serializer = NoteSerializer(notes, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def getTcourses(request):

    tcourses = Tcourse.objects.all()
    serializer = TcourseSerializer(tcourses, many=True)
    return Response(serializer.data)
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    
    
@api_view(['GET'])
def getEvents(request):
    events = generate_events(os.path.dirname(os.path.realpath(__file__)) + '\\mock_data.csv')
    return Response(events)