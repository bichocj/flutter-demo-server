from rest_framework import viewsets
from . import serializers, models

class ClientViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = serializers.ClientSerializer
    queryset = models.Client.objects.all()