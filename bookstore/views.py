from django.shortcuts import render
from requests import get, post, patch, delete
from . models import Books
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from . serializers import BooksSerializer
from rest_framework.permissions import AllowAny


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
        serializer = BooksSerializer(books, many=True)
        
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







