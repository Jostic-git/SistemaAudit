from django.db import models


# Справочная информация системы

# активы АФК (организации)
class Company(models.Model):
    short_name = models.CharField(max_length=150, verbose_name='Короткое название')
    full_name = models.CharField(max_length=150, verbose_name='Полное название')
    inn = models.IntegerField(verbose_name='ИНН компании')

    class Meta:
        ordering = ['short_name']

    def __str__(self):
        return self.short_name


# данные по активу
class ActiveData(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='companies', verbose_name='Организация')
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


# риски
class Risk(models.Model):
    title = models.CharField(max_length=200, verbose_name='Наименование риска')


# Процессы 1 уровня
class Process(models.Model):
    title = models.CharField(max_length=200, verbose_name='Наименование процесса')


# Подпроцессы
class SubProcess(models):
    process = models.ForeignKey(Process, related_name='processes', verbose_name='Процесс верхнего уровня')
    title = models.CharField(max_length=200, verbose_name='Наименование подпроцесса')

