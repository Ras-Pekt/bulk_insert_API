from rest_framework import serializers
from .models import Product, ProductVariant


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ["id", "sku", "name", "price"]


class ProductSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True)

    class Meta:
        model = Product
        fields = ["id", "name", "image", "variants"]

    def create(self, validated_data):
        variants_data = validated_data.pop("variants")
        product = Product.objects.create(**validated_data)
        variants = [
            ProductVariant(product_id=product, **variant_data)
            for variant_data in variants_data
        ]
        ProductVariant.objects.bulk_create(variants)
        return product
