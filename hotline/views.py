import datetime

from rest_framework import viewsets, status
from rest_framework.response import Response

from hotline.models import HotLineItem, CategoryHotLine, SubCategoryHotLine, HotLineFile, HotLineComment
from hotline.serializers import HotLineItemSerializer, CategoryHotLineSerializer, SubCategoryHotLineSerializer, \
    HotLineFileSerializer, HotLineCommentSerializer


class CategoryHotLineViewSet(viewsets.ModelViewSet):
    queryset = CategoryHotLine.objects.all()
    serializer_class = CategoryHotLineSerializer
    # permission_classes = [IsAuthenticated]


class SubCategoryHotLineViewSet(viewsets.ModelViewSet):
    queryset = SubCategoryHotLine.objects.all()
    serializer_class = SubCategoryHotLineSerializer
    # permission_classes = [IsAuthenticated]


class HotLineFileViewSet(viewsets.ModelViewSet):
    queryset = HotLineFile.objects.all()
    serializer_class = HotLineFileSerializer
    # permission_classes = [IsAuthenticated]


class HotLineCommentViewSet(viewsets.ModelViewSet):
    queryset = HotLineComment.objects.all()
    serializer_class = HotLineCommentSerializer
    # permission_classes = [IsAuthenticated]


class HotLineItemViewSet(viewsets.ModelViewSet):
    queryset = HotLineItem.objects.all()
    serializer_class = HotLineItemSerializer

    # permission_classes = [IsAuthenticated]

