from django.db import models


# Reference book

# AFK Companies
class Company(models.Model):
    short_name = models.CharField(max_length=150, verbose_name='Shot name')
    full_name = models.CharField(max_length=150, verbose_name='Full name')
    inn = models.IntegerField(verbose_name='INN')

    class Meta:
        ordering = ['short_name']

    def __str__(self):
        return self.short_name


# Company data
class ActiveData(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                related_name='active_data_companies',
                                verbose_name='Организация')
    period = models.IntegerField(verbose_name='Период показателей')
    actives = models.FloatField(verbose_name='Активы организации')
    earn = models.FloatField(verbose_name='Выручка')
    cost_price = models.FloatField(verbose_name='Себестоимость')
    oibda = models.FloatField(verbose_name='OIBDA')
    net_profit = models.FloatField(verbose_name='Чистая прибыль')
    count_employee = models.IntegerField(verbose_name='Количество сотрудников')
    count_employee_ia = models.IntegerField(verbose_name='Количество сотрудников ВА')
    budget_ia = models.FloatField(verbose_name='Бюджет ВА')
    costs_ia = models.FloatField(verbose_name='Затраты ВА')

    class Meta:
        ordering = ['period']


# Risks
class Risk(models.Model):
    title = models.CharField(max_length=200, verbose_name='Наименование риска')


# Process 1 level
class Process(models.Model):
    title = models.CharField(max_length=200, verbose_name='Наименование процесса')


# Subprocess
class SubProcess(models.Model):
    process = models.ForeignKey(Process, on_delete=models.CASCADE,
                                related_name='processes',
                                verbose_name='Процесс верхнего уровня')
    title = models.CharField(max_length=200, verbose_name='Наименование подпроцесса')