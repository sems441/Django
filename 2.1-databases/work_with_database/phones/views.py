from django.shortcuts import render, redirect
from models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sorted_items = request.Get.get("sort")
    phones_query = Phone.objects.all()
    if sorted_items == "name":
        pass
    elif sorted_items == "min_price":
        pass
    elif sorted_items == "max_price":
        pass
    context = {
        "phones": phones_query,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
