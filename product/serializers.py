from rest_framework import serializers

from .models import Product,Category

class ProductSerializer(serializers.ModelSerializer):
    """serilizer for managing product """
    class Meta:
        model = Product
        fields = '__all__'

class CatSerializer(serializers.ModelSerializer):
    """For creating or managing the categotry"""

    class Meta:
        model = Category
        fields = '__all__'