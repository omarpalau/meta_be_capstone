from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import MenuItemSerializer
from .models import MenuItem

# Create your views here.

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer