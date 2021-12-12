from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import request
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrViewOnly
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrViewOnly]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filter_class = AdvertisementFilter

    filterset_fields = ['creator__id', 'id']
    search_field = ['id']
