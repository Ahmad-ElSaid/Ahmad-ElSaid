from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Todolist
from .serializers import *

@api_view(['GET', 'POST'])
def todolist_list(request):
    if request.method == 'GET':
        data = Todolist.objects.all()

        serializer = TodolistSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TodolistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


@api_view(['PUT','DELETE'])
def todolist_detail(request, id):
    try:
        todolist = Todolist.objects.get(id=id)
    except Todolist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TodolistSerializer(todolist, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        todolist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
