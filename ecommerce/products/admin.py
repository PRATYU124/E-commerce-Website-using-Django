from django.contrib import admin
from .models import Category, Product, QuantityVariant, ColorVariant, SizeVariant, ProductImages

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(QuantityVariant)
admin.site.register(ColorVariant)
admin.site.register(SizeVariant)
admin.site.register(ProductImages)




