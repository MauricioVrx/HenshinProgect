from django import views
from django.shortcuts import render
from django.views import generic

from .models import Product

class IndexView(generic.ListView):
    template_name="product/index.html"
    context_object_name = "latest_products_list"

    def get_queryset(self):
        """ Return the last five published products """
        return Product.objects.order_by("-created_date").filter(status = True)[:5]

# def index(request):
#     return render(request,"product/index.html", {} )