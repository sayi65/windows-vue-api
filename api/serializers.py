from rest_framework import serializers
from api.models import User

class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ('id', 'emp_code', 'emp_name', 'email', 'created')