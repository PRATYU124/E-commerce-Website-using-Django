from django.db import models
from django.utils.text import slugify

# Category model
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, blank=True, unique=True)
    image=models.ImageField(upload_to='static/category' ,blank=True)

    def save(self, *args, **kwargs):  # No Error Here
        if not self.slug:
            self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category_name


# Quantity Variant model
class QuantityVariant(models.Model):
    Variant_name = models.CharField(max_length=50)

    def __str__(self):  
        return self.Variant_name


# Color Variant model
class ColorVariant(models.Model):
    color_name = models.CharField(max_length=100)
    color_code=models.CharField(max_length=100)
    # Missing color_code field, if required
    # If you do not need it, this is fine.

    def __str__(self):  # No Error Here
        return self.color_name


# Size Variant model
class SizeVariant(models.Model):
    size_name = models.CharField(max_length=50)

    def __str__(self):  # No Error Here
        return self.size_name


# Product model
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE ,default=1)
    product_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/products',)
    price = models.CharField(max_length=20)
    description = models.TextField()
    stock = models.PositiveIntegerField(default=100)

    quantity_type=models.ForeignKey(QuantityVariant, blank=True, null=True, on_delete=models.PROTECT)
    color_type=models.ForeignKey(ColorVariant, blank=True, null=True, on_delete=models.PROTECT)
    size_type=models.ForeignKey(SizeVariant, blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.product_name          

class ProductImages(models.Model):
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    image=models.ImageField(upload_to='static/products',default='path/to/default/image.jpg')

