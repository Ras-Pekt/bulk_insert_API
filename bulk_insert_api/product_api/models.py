from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256)
    image = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    sku = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    details = models.TextField()
    product_id = models.ForeignKey(
        Product, related_name="variants", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.name} ({self.sku})"
