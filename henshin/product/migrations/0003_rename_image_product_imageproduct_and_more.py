# Generated by Django 4.0.3 on 2022-03-16 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_image_product_url_alter_product_price_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image_product',
            new_name='ImageProduct',
        ),
        migrations.RenameModel(
            old_name='Size_product',
            new_name='SizeProduct',
        ),
        migrations.RenameModel(
            old_name='Stock_product',
            new_name='StockProduct',
        ),
        migrations.RenameModel(
            old_name='Type_product',
            new_name='TypeProduct',
        ),
    ]
