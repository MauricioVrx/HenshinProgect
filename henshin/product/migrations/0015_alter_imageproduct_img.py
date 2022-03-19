# Generated by Django 4.0.3 on 2022-03-19 18:51

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_rename_url_imageproduct_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageproduct',
            name='img',
            field=models.FileField(null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='product'),
        ),
    ]
