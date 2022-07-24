from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import User, Shop
from .serializers import UserSerializer, ShopSerializer

# Create your views here.

class UserApiView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ShopApiView(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

