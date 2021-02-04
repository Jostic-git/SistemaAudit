# Generated by Django 3.1.2 on 2021-01-27 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotline', '0002_auto_20210127_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotlineitem',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='System user'),
        ),
        migrations.AlterField(
            model_name='hotlineitem',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Новое'), (1, 'В работе'), (2, 'Завершено')], default=0, verbose_name='Forwarded item status'),
        ),
    ]