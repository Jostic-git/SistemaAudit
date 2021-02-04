from django.db import models
from reference.models import Company, Risk, SubProcess


# Приложение "оценка рисков"

# оценка риска
class RiskAssessment(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                related_name='risk_assessment_companies',
                                verbose_name='Организация')
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE, related_name='risks', verbose_name='Риск')
    sub_process = models.ForeignKey(SubProcess, on_delete=models.CASCADE,
                                    related_name='sub_processes',
                                    verbose_name='Подпроцесс')
    probability = models.IntegerField(verbose_name='Вероятность')
    impact = models.IntegerField(verbose_name='Влияние на процесс')
