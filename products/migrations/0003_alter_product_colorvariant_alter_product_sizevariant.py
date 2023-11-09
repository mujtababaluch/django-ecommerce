# Generated by Django 4.2.1 on 2023-09-01 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_colorvariant_sizevariant_product_colorvariant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ColorVariant',
            field=models.ManyToManyField(blank=True, to='products.colorvariant'),
        ),
        migrations.AlterField(
            model_name='product',
            name='SizeVariant',
            field=models.ManyToManyField(blank=True, to='products.sizevariant'),
        ),
    ]
