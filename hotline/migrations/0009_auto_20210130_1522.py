# Generated by Django 3.1.2 on 2021-01-30 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotline', '0008_auto_20210130_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotlineitem',
            name='closed',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Closed date'),
        ),
    ]
