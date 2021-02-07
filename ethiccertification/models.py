from django.db import models

from reference.models import Company


class EthicItem(models.Model):
    STATUS_ETHIC_ITEM = (
        (0, 'New'),
        (1, 'Need action'),
        (2, 'Finished')
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name='Create date')
    edited = models.DateTimeField(auto_now=True, verbose_name='Edit date')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Company')
    employee = models.CharField(max_length=100, verbose_name='Employee name')
    employee_position = models.CharField(max_length=100, verbose_name='Employee position')
    status = models.SmallIntegerField(choices=STATUS_ETHIC_ITEM, verbose_name='Status ethic item', default=0)
    answer_1 = models.BooleanField(verbose_name='question_1')
    answer_1_comment = models.TextField(null=True, blank=True, verbose_name='question 1 comment')
    answer_2 = models.BooleanField(verbose_name='question_2')
    answer_3 = models.BooleanField(verbose_name='question_3')
    answer_4 = models.BooleanField(verbose_name='question_4')
    answer_5 = models.BooleanField(verbose_name='question_5')
    answer_6 = models.BooleanField(verbose_name='question_6')
    answer_6_comment = models.TextField(null=True, blank=True, verbose_name='question 6 comment')
    answer_7 = models.BooleanField(verbose_name='question_7')
    answer_7_comment = models.TextField(null=True, blank=True, verbose_name='question 7 comment')
    answer_8 = models.BooleanField(verbose_name='question_8')
    answer_8_comment = models.TextField(null=True, blank=True, verbose_name='question 8 comment')
    answer_9 = models.BooleanField(verbose_name='question_9')
    answer_9_comment = models.TextField(null=True, blank=True, verbose_name='question 9 comment')
    answer_10 = models.BooleanField(verbose_name='question_10')
    answer_10_comment = models.TextField(null=True, blank=True, verbose_name='question 10 comment')
    questionnaire_file = models.FileField(upload_to='project_files', null=True, max_length=255)

    def __str__(self):
        return f'Анкета №{self.id} {self.employee} от {self.created} ({self.company.short_name})'

    class Meta:
        ordering = ['status', '-created']


# конкретика по вопросам если отвечено "Да"

class EthicItemAnswer2(models.Model):
    STATUS_RELATION_CHOICES = (
        (0, 'Я'),
        (1, 'Родственник'),
        (2, 'Доверенный представитель')
    )
    STATUS_RELATION_CORPORATION = (
        (0, 'Не в группе АФК'),
        (1, 'В группе АФК')
    )
    ethic_item = models.ForeignKey(EthicItem, related_name='ethic_item_answers_2', on_delete=models.CASCADE,
                                   verbose_name='Ethic item')
    relation_status = models.SmallIntegerField(choices=STATUS_RELATION_CHOICES, verbose_name='Relations status')
    FIO = models.CharField(max_length=100, verbose_name='FIO')
    share_of_capital = models.SmallIntegerField(verbose_name='Share of capital, %')
    relation_to_corporation = models.SmallIntegerField(choices=STATUS_RELATION_CORPORATION,
                                                       verbose_name='Relation to AFK', default=0)
    company_name = models.CharField(max_length=100, null=True, verbose_name='Company name')
    company_INN = models.CharField(max_length=10, null=True, blank=True, verbose_name='Company INN')
    comment = models.TextField(null=True, blank=True, verbose_name='Comment')

    def __str__(self):
        return f'Ответ на вопрос 3 №{self.ethic_item.id} {self.ethic_item.employee} ({self.ethic_item.company})'


class EthicItemAnswer3(models.Model):
    STATUS_RELATION_CHOICES = (
        (0, 'Я'),
        (1, 'Родственник'),
        (2, 'Доверенный представитель')
    )
    ethic_item = models.ForeignKey(EthicItem, related_name='ethic_item_answers_3', on_delete=models.CASCADE,
                                   verbose_name='Ethic item')
    relation_status = models.SmallIntegerField(choices=STATUS_RELATION_CHOICES, verbose_name='Relations status')
    FIO = models.CharField(max_length=100, verbose_name='FIO')
    comment = models.TextField(null=True, blank=True, verbose_name='Comment')

    def __str__(self):
        return f'Ответ на вопрос 3 №{self.ethic_item.id} {self.ethic_item.employee} ({self.ethic_item.company})'


class EthicItemAnswer4(models.Model):
    STATUS_RELATION_CHOICES = (
        (0, 'Я'),
        (1, 'Родственник'),
        (2, 'Доверенный представитель')
    )
    ethic_item = models.ForeignKey(EthicItem, related_name='ethic_item_answers_4', on_delete=models.CASCADE,
                                   verbose_name='Ethic item')
    relation_status = models.SmallIntegerField(choices=STATUS_RELATION_CHOICES, verbose_name='Relations status')
    FIO = models.CharField(max_length=100, verbose_name='FIO')
    comment = models.TextField(null=True, blank=True, verbose_name='Comment')

    def __str__(self):
        return f'Ответ на вопрос 4 №{self.ethic_item.id} {self.ethic_item.employee} ({self.ethic_item.company})'


class EthicItemAnswer5(models.Model):
    ethic_item = models.ForeignKey(EthicItem, related_name='ethic_item_answers_5', on_delete=models.CASCADE,
                                   verbose_name='Ethic item')
    degree = models.CharField(max_length=100, verbose_name='Degree (in family)')
    FIO = models.CharField(max_length=100, verbose_name='FIO')
    position = models.CharField(max_length=100, verbose_name='Position in company')
    impact = models.BooleanField(verbose_name='Impact yes/no')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Company')
    comment = models.TextField(null=True, blank=True, verbose_name='Comment')