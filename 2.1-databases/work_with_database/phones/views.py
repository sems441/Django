from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sorted_items = request.GET.get("sort")
    phones_query = Phone.objects.all()
    if sorted_items == "name":
        phones_query = phones_query.order_by("name")
    elif sorted_items == "min_price":
        phones_query = phones_query.order_by("price")
    elif sorted_items == "max_price":
        phones_query = phones_query.order_by("-price")
    context = {
        "phones": phones_query,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones_query = Phone.objects.get(slug=slug)
    context = {
        "phone": phones_query
    }
    return render(request, template, context)
