from api.models import User, WorkTime
from api.serializers import WorkTimeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework import generics


# Create your views here.
class WorkTimeListView(generics.ListCreateAPIView):    
    queryset = User.objects.all()
    serializer_class = WorkTimeSerializer
    filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('id', 'emp_code', 'emp_name', 'email', 'created',)

class WorkTimeDetailView(generics.RetrieveUpdateDestroyAPIView):    
    queryset = WorkTime.objects.all()
    serializer_class = WorkTimeSerializer
    # filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('id', 'emp_code', 'emp_name', 'email', 'created',)