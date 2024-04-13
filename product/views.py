from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from .serializers import ProductSerializer, CatSerializer
from .models import Product, Category

class ProductViewSet(viewsets.ModelViewSet):
    """ view for managing product """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CatViewSet(viewsets.ModelViewSet):
    """ view for managing category"""

    queryset = Category.objects.all()
    serializer_class = CatSerializer