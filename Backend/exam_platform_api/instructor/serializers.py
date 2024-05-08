from rest_framework import serializers
from .models import Instructor

class InstructorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Instructor
        fields = ['is_instructor']