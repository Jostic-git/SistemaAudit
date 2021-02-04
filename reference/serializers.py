from rest_framework import serializers

from reference.models import Company, Risk, Process, SubProcess


# организация
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'short_name', 'full_name', 'inn']


# риски
class RiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Risk
        fields = ['id', 'title']


# подпроцессы
class SubProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubProcess
        fields = ['id', 'process', 'title']


# процессы первого уровня с подпроцесами
class ProcessSerializer(serializers.ModelSerializer):
    processes = SubProcessSerializer(many=True, read_only=True)

    class Meta:
        model = Process
        fields = ['id', 'title']
