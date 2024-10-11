from rest_framework import serializers
from .models import Product, ProductVariant
from django.db import transaction


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True)

    class Meta:
        model = Product
        fields = ["id", "name", "image", "variants"]

    def create(self, validated_data):
        variants_data_list = []
        products_data = []

        for product_data in validated_data:
            variants_data = product_data.pop("variants")
            product = Product(**product_data)
            products_data.append(product)

            for variant_data in variants_data:
                variant_data["product_id"] = product
                variants_data_list.append(variant_data)

        with transaction.atomic():
            products = Product.objects.bulk_create(products_data)

            variants = [
                ProductVariant(product=product, **variant_data)
                for product, variant_data in zip(products, variants_data_list)
            ]

            ProductVariant.objects.bulk_create(variants)

        return products
