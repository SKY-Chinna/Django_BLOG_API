from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import ProductSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework import serializers


# Create your views here.
@api_view(['GET'])
def get(request):
  x =Product.objects.all()
  serializer = ProductSerializer(x, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def View(request,id):
  x =Product.objects.get(id=id)
  serializer = ProductSerializer(x)
  return Response(serializer.data)

@api_view(['POST'])
def create(request):
  # x=book.objects.all()  # query set
  serializer=ProductSerializer(data=request.data)
  if serializer.is_valid():
     serializer.save()
  return Response(serializer.data)




@api_view(['PUT'])
def Update(request, id):
  x=Product.objects.get(id=id)  # query set
  serializer=ProductSerializer(instance=x,data=request.data)
  if serializer.is_valid():
     serializer.save()
  return Response(serializer.data)

@api_view(['DELETE'])
def delete(request, id):
  Books=Product.objects.get(id=id)  # query set
  Books.delete()
  return Response("successfully deleted")


