# carts/serializers.py
from rest_framework import serializers
from .models import CartItems, Cart
# Removed the ProductSerializer import to avoid circular import
# from products.serializers import ProductSerializer
from .models import Orders



class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartItemsSerializer(serializers.ModelSerializer):
    # Lazy import to avoid circular imports
    def get_product_serializer(self):
        from products.serializers import ProductSerializer
        return ProductSerializer()

    cart = CartSerializer()
    product = serializers.SerializerMethodField()  # Use the method to get the product serializer

    class Meta:
        model = CartItems
        fields = '__all__'

    def get_product(self, obj):
        return self.get_product_serializer().to_representation(obj.product)
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        models = Orders
        fields='__all__'