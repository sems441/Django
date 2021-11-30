from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


# class MyDjangoFilterBackend(DjangoFilterBackend):
#     serializer_class = ProductSerializer
#
#     filter_backends = [SearchFilter]
#     search_fields = ['title']
#     def get_filterset(self, request, queryset, view):


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [SearchFilter]
    search_fields = ['title']

    pagination_class = LimitOffsetPagination


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['products']
    filter_backends = [SearchFilter]
    search_fields = ['products__title']

