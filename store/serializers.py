from rest_framework import serializers
from decimal import Decimal
from playground.models import Product, Collection
from store.models import Review


class CollectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products-count']
    products_count = serializers.IntegerField(read_only=True)


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price', 'price_with_tax', 'collection']

    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'date', 'name', 'description', 'product']
