from django.shortcuts import render
from rest_framework import viewsets

from reference.models import Company, Risk, Process, SubProcess
from reference.serializers import CompanySerializer, RiskSerializer, ProcessSerializer, SubProcessSerializer


# CRUD организации, переопределить метод удаления
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    # permission_classes = [IsAuthenticated]


# CRUD риски
class RiskViewSet(viewsets.ModelViewSet):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer
    # permission_classes = [IsAuthenticated]


# CRUD Процессы верхнего уровня
class ProcessViewSet(viewsets.ModelViewSet):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer
    # permission_classes = [IsAuthenticated]


# CRUD подпроцессы
class SubProcessViewSet(viewsets.ModelViewSet):
    queryset = SubProcess.objects.all()
    serializer_class = SubProcessSerializer
    # permission_classes = [IsAuthenticated]
