import datetime

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from reference.models import Company
from django.contrib.auth import get_user_model

User = get_user_model()


# hot line category (for all companies)
class CategoryHotLine(models.Model):
    title = models.CharField(max_length=100, verbose_name='Category name')

    def __str__(self):
        return self.title


# hot line subcategory for each companies
class SubCategoryHotLine(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='companies', verbose_name='Company')
    category = models.ForeignKey(CategoryHotLine, on_delete=models.CASCADE, verbose_name='Hotline category')
    title = models.CharField(max_length=100, verbose_name='Subcategory name')
    responsible_employee = models.CharField(max_length=200, null=True, blank=True, verbose_name='Responsible Employee')

    def __str__(self):
        return self.title


def get_close_date_by_status(status: int):
    if status == 2:
        return datetime.datetime.now()
    else:
        return None


class HotLineItem(models.Model):
    """
    Hotline item model
    """
    HOTLINE_CHANNEL = (
        (1, 'Электронная почта Актива'),
        (2, 'Электронная почта Корпорации'),
        (3, 'Бумажная почта'),
        (4, 'Лично'),
        (5, 'Форма обратной связи на сайте'),
        (6, 'Телефонный звонок')
    )
    STATUS_ITEM = (
        (0, 'Новое'),
        (1, 'В работе'),
        (2, 'Завершено')
    )
    STATUS_ANSWER = (
        (0, 'Информация подтвердилась'),
        (1, 'Информация подтвердилась частично'),
        (2, 'Информация не подтвердилась')
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='hotlineitems', verbose_name='Company')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created date, time')
    creator = models.ForeignKey(User, related_name='user', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='System user')
    received = models.DateField(verbose_name='Received date')
    channel = models.SmallIntegerField(choices=HOTLINE_CHANNEL, default=1, verbose_name='Received channel')
    sub_category = models.ForeignKey(SubCategoryHotLine, on_delete=models.SET_NULL, null=True,
                                     verbose_name='Hotline subcategory')
    received_text = models.TextField(blank=True, null=True, verbose_name='Core of the problem')
    client_contact = models.CharField(max_length=200, verbose_name='Contacts client')
    forwarded = models.DateField(null=True, blank=True, verbose_name='Forwarded date')
    forwarded_to_emp = models.CharField(max_length=200, null=True, blank=True,
                                        verbose_name='Employee whom forwarded item')
    status = models.SmallIntegerField(choices=STATUS_ITEM, verbose_name='Forwarded item status', default=0)
    action = models.CharField(max_length=300, blank=True, null=True, verbose_name='Action by answer')
    status_answer = models.SmallIntegerField(choices=STATUS_ANSWER, null=True, blank=True, verbose_name='Answer status',
                                             default=0)
    closed = models.DateTimeField(null=True, blank=True, verbose_name='Closed date')
    damage = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return f'Сообщение № {self.id} от {self.client_contact}'

    class Meta:
        ordering = ['status']


@receiver(pre_save, sender=HotLineItem)
def default_subject(sender, instance, **kwargs):
    if not instance.closed and instance.status == 2:
        instance.closed = datetime.datetime.now()


class HotLineFile(models.Model):
    '''
    Hotline file items
    '''
    hotline_item = models.ForeignKey(HotLineItem, on_delete=models.CASCADE, related_name='hotline_files')
    file = models.FileField()


#    def __str__(self):
#        return self.hotline_item


class HotLineComment(models.Model):
    '''
    hotline comments
    '''
    hotline_item = models.ForeignKey(HotLineItem, on_delete=models.CASCADE, related_name='hotline_comments')
    comment = models.TextField(verbose_name='Comment')
    created = models.DateTimeField(auto_now=True, verbose_name='Comment date')
    user_name = models.CharField(max_length=100, verbose_name='User name', null=True)

    def __str__(self):
        return self.comment[:50]
