from rest_framework.serializers import ModelSerializer
from base.models import Note
from base.models import Tcourse

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        
class TcourseSerializer(ModelSerializer):
    class Meta:
        model = Tcourse
        fields = 'all'
        
