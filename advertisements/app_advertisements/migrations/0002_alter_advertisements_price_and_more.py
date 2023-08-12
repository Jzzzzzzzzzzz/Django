# Generated by Django 4.2.3 on 2023-08-09 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisements',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=100, verbose_name='цена'),
        ),
        migrations.AlterModelTable(
            name='advertisements',
            table='Advertisements',
        ),
    ]