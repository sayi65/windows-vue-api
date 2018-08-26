from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from api.models import User
from api.serializers import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class UserListViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('emp_code', 'emp_name', 'email', 'created',)


    # def get_queryset(self):
    #     return User.objects.all()

    # def get(self, request, format=None):
    #     """
    #     List all code snippets, or create a new snippet.
    #     """
    #     if request.method == 'GET':
    #         users = User.objects.all()
    #         serializer = UserSerializer(users, many=True)
    #         filter_backends = (DjangoFilterBackend,)
    #         filter_fields = ('emp_code', 'emp_name', 'email', 'created')
    #         return JsonResponse(serializer.data, safe=False)
    
    # def post(self, request, format=None):
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserDetail(generics.ListCreateAPIView):
    
#     def get_objects(self, pk):
#         try:
#             return User.objects.get(emp_code=pk)
#         except User.DoesNotExist:
#             raise Http404
    
#     def get(self, request, pk, format=None):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         filter_backends = (DjangoFilterBackend,)
#         filter_fields = ('emp_code', 'emp_name', 'email', 'created')
#         # return Response(serializer.data)
    
#     def put(self, request, pk, format=None):
#         user = self.get_objects(pk)
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk, format=None):
#         user = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)