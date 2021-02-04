# Generated by Django 3.1.2 on 2021-01-27 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0002_auto_20210127_1736'),
        ('hotline', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryHotLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Category name')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategoryHotLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Subcategory name')),
                ('responsible_employee', models.CharField(blank=True, max_length=200, null=True, verbose_name='Responsible Employee')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotline.categoryhotline', verbose_name='Hotline category')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='reference.company', verbose_name='Company')),
            ],
        ),
        migrations.AlterField(
            model_name='hotlineitem',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotline.subcategoryhotline', verbose_name='Hotline subcategory'),
        ),
    ]