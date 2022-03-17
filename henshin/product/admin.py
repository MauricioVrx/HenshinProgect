from django.contrib import admin
from .models import TypeProduct, SizeProduct, ColorProduct, StockProduct, ImageProduct, Product, ProductStock, Tag 
# ProductTag

admin.site.register(TypeProduct)
admin.site.register(SizeProduct)
admin.site.register(ColorProduct)
admin.site.register(StockProduct)
admin.site.register(ImageProduct)
admin.site.register(Product)
admin.site.register(ProductStock)
admin.site.register(Tag)
# admin.site.register(ProductTag)
