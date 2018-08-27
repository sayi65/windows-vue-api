from rest_framework import viewsets, status
from api.models import User
from api.serializers import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class UserListViewSet(viewsets.ModelViewSet):    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id','emp_code', 'emp_name', 'email', 'created',)
    http_method_names = ['get', 'post', 'delete' ,'head']
    lookup_field = 'emp_code'

    @action(detail=True)
    def group_names(self, request, pk=None):
        user = self.get_object()
        groups = user.groups.all()
        return Response([group.name for group in groups])

    # @action(methods=['delete'], detail=False)
    # def set_password(self, request, pk=None):
    #     user = self.get_object()
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         user.set_password(serializer.data['password'])
    #         user.save()
    #         return Response({'status': 'password set'})
    #     else:
    #         return Response(serializer.errors,
    #                         status=status.HTTP_400_BAD_REQUEST)