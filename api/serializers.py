from rest_framework import serializers
from api.models import User, WorkTime

class UserSerializer(serializers.ModelSerializer):
    def __str__(self):
        return u'%s' % (self.emp_code)
    class Meta:
        model = User
        fields = ('id', 'emp_code', 'emp_name', 'email', 'updated','created',)

class WorkTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkTime
        fields = ('id', 'pj_name', 'reason', 'wk_reason', 'overtime','updated','created')
