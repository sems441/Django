from rest_framework.viewsets import ModelViewSet
from rest_framework.status import HTTP_200_OK
from measurements.models import Project, Measurement
from serializers import ProjectSerializers, MeasurementSerializers
from rest_framework.response import Response


class ProjectViewSet(ModelViewSet):
    """ViewSet для проекта."""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers


class MeasurementViewSet(ModelViewSet):
    """ViewSet для измерения."""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializers
