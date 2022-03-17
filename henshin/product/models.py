
from django.db import models
from django.forms import CharField


class TypeProduct(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50,     blank=True , default="")
    icon = models.CharField(max_length=255,    blank=True , default="")
    material = models.CharField(max_length=50, blank=True , default="")

    def __str__(self):
        if len(self.type) == 0:
            return (f"{self.name}")
        return (f"{self.name} - {self.type}")
    

class SizeProduct(models.Model):
    type_product = models.ForeignKey(TypeProduct, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50, blank=True, default="")
    lenght = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)
    width  = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)
    heigh  = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)
    pac_lenght = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)
    pac_width  = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)
    pac_heigh  = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)
    weight = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return (f"{self.name} - {self.type_product}")


class ColorProduct(models.Model):
    name = models.CharField(max_length=50)
    hex  = models.CharField(max_length=6)

    def __str__(self):
        return (f"{self.name}") 

    
class StockProduct(models.Model):
    size_product  = models.ForeignKey(SizeProduct   , on_delete=models.PROTECT)
    color_product = models.ForeignKey(ColorProduct  , on_delete=models.PROTECT)
    stock     = models.IntegerField(default = 0)
    min_stock = models.IntegerField(default = 0)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True )
    updated_date = models.DateTimeField(auto_now=True , auto_now_add=False)
    status = models.BooleanField(default = True)

    def __str__(self):
        return (f"{self.size_product} {self.color_product} : {self.stock}")

    def is_low(self):
        return not(self.stock > self.min_stock)


class ImageProduct(models.Model):
    name = models.CharField(max_length=50)
    url  = models.TextField(null = True)
    description = models.CharField(max_length=50, blank=True)
    type = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return (f"{self.name}")

class Tag(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)

    def __str__(self):
        return(f"{self.name}")


class Product(models.Model):
    main_image =  models.ForeignKey(ImageProduct, on_delete=models.PROTECT, null = True, blank = True)
    tag   =  models.ManyToManyField(Tag)
    name  = models.CharField(max_length=20)
    price = models.IntegerField(default = 13990)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True )
    updated_date = models.DateTimeField(auto_now=True , auto_now_add=False)
    status = models.BooleanField(default = True)
    selled = models.IntegerField(default = 0)

    def __str__(self):
        return (f"{self.name}")


class ProductStock(models.Model):
    model     = models.CharField(max_length = 20, blank=True, default="")
    product       = models.ForeignKey(Product       , on_delete=models.CASCADE)
    image         = models.ForeignKey(ImageProduct  , on_delete=models.PROTECT)
    stock_product = models.ForeignKey(StockProduct  , on_delete=models.CASCADE)
    status = models.BooleanField(default = True)
    created_date  = models.DateTimeField(auto_now=False, auto_now_add=True )
    updated_date  = models.DateTimeField(auto_now=True , auto_now_add=False)

    def __str__(self):
        return (f"{self.product} {self.stock_product} : {self.product.price}")




# class ProductTag(models.Model):
#     tag     = models.ForeignKey(Tag     , on_delete=models.CASCADE)
#     product = models.ForeignKey(Product , on_delete=models.CASCADE)
#     created_date  = models.DateTimeField(auto_now=False, auto_now_add=True )
#     updated_date  = models.DateTimeField(auto_now=True , auto_now_add=False)

#     def __str__(self):
#         return(f"{self.product} - {self.tag}")
