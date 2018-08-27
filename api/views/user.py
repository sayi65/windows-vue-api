from api.models import User
from api.serializers import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework import generics


# Create your views here.
class UserListView(generics.ListCreateAPIView):    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'emp_code', 'emp_name', 'email', 'created',)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'emp_code', 'emp_name', 'email', 'created',)