# Generated by Django 3.1.2 on 2021-01-27 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotline', '0003_auto_20210127_2202'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hotlineitem',
            options={'ordering': ['status']},
        ),
        migrations.AddField(
            model_name='hotlineitem',
            name='closed',
            field=models.DateField(blank=True, null=True, verbose_name='Closed date'),
        ),
    ]
