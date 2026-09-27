from django.shortcuts import render
from requests import get, post, patch, delete
from . models import Books
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from . serializers import BooksSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view


from django.contrib.auth.models import User
from .serializers import UserSerializer






class BookListView(APIView):
    #permission_classes = [AllowAny
    http_method_names = ['get', 'post', 'delete', 'patch']
    def post(self, request):
        model = Books
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,
                status=status.HTTP_201_CREATED
                )
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        books = Books.objects.all()
        serializer = BooksSerializer(books, many=True,context={'request':request})
        
        return Response(serializer.data)
    
    
    def patch(self, request, pk=None):
        obj = self.get_object(pk)
        serializer = BooksSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk=None):
        obj = self.get_object(pk)
        obj.delete()
  
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
    
@api_view(['POST','GET'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    print(username, password)
    
    user = authenticate(username=username, password=password)
    
    if user is not None:
        token,_= Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user':{
                'id':user.id,
                'username': user.username,
                'email': user.email
                }
        })
    else:
        return Response({
            'detail':'Invalid username or passsword'},
            status=status.HTTP_401_UNAUTHORIZED)
        

'''
@api_view(['POST','GET'])
def users(request):
    if request.method == 'GET':
        from django.contrib.auth.models import User
        from .serializers import UserSerializer
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    if request.method == 'POST':
        serializer  = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
       '''
'''
class LoginView(APIView):      
        
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,
                status=status.HTTP_201_CREATED
                )
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        users =User.objects.all()
        serializer = BooksSerializer(users, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
        
'''





