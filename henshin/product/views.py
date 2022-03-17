from django import views
from django.shortcuts import render
from django.views import generic

class IndexView(generic.ListView):
    template_name="product/index.html"

    def get_queryset(self):
        pass

# def index(request):
#     return render(request,"product/index.html", {} )