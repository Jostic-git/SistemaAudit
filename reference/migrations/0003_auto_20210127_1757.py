# Generated by Django 3.1.2 on 2021-01-27 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotline', '0002_auto_20210127_1757'),
        ('reference', '0002_auto_20210127_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategoryhotline',
            name='category',
        ),
        migrations.RemoveField(
            model_name='subcategoryhotline',
            name='company',
        ),
        migrations.DeleteModel(
            name='CategoryHotLine',
        ),
        migrations.DeleteModel(
            name='SubCategoryHotLine',
        ),
    ]
