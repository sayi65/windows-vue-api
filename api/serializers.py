from rest_framework import serializers
from api.models import User, WorkTime

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class WorkTimeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WorkTime
        fields = '__all__'