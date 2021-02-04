from rest_framework import viewsets

from ethiccertification.models import EthicItem
from ethiccertification.serializers import EthicItemSerializer


class EthicItemViewSet(viewsets.ModelViewSet):
    queryset = EthicItem.objects.all()
    serializer_class = EthicItemSerializer
