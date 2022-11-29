from rest_framework.serializers import ModelSerializer
from base.models import Note
from base.models import Tcourse, Tcourseevent, Tpersonalevent, Tschedule, Tstudent, Tstudentcourse, Ttimeslot


from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from rest_framework.permissions import AllowAny




class RegisterSerializer(ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user


class CourseSerializer(ModelSerializer):
    
    #add a custom field which takes a string input
    custom_field = serializers.CharField(write_only=True, required=True)
    
    
    class Meta:
        model = Tstudentcourse
        #fields will accept custom field and all fields from Tstudentcourse
        fields = ['custom_field', 'course']
    
    def validate(self, attrs):
        #convert custom field to student object
        attrs['student'] = User.objects.get(username=attrs['custom_field'])
        return attrs
    
    
    def create(self, validated_data):
        # convert student field to user object
        print("create ran on " + str(validated_data))
        try:
            tstudentcourse = Tstudentcourse.objects.create(
                student=validated_data['student'],
                course=validated_data['course'],
            )
            
            tstudentcourse.save()
            return tstudentcourse
        except:
            return None

class NoteSerializer(ModelSerializer):
    
    class Meta:
        model = Note
        fields = '__all__'
        
class TcourseSerializer(ModelSerializer):
    class Meta:
        model = Tcourse
        fields = '__all__'

#create a serializer for Tcourseevent, Tpersonalevent, Tschedule, Tstudent, Tstudentcourse, Ttimeslot

class TcourseeventSerializer(ModelSerializer):
    class Meta:
        model = Tcourseevent
        fields = '__all__'

class TpersonaleventSerializer(ModelSerializer):
    class Meta:
        model = Tpersonalevent
        fields = '__all__'
        
class TscheduleSerializer(ModelSerializer):
    class Meta:
        model = Tschedule
        fields = '__all__'

class TstudentSerializer(ModelSerializer):
    class Meta:
        model = Tstudent
        fields = '__all__'

class TstudentcourseSerializer(ModelSerializer):
    class Meta:
        model = Tstudentcourse
        fields = '__all__'
        
class TtimeslotSerializer(ModelSerializer):
    class Meta:
        model = Ttimeslot
        fields = '__all__'



