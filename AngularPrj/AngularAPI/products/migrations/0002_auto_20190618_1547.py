# Generated by Django 2.2.1 on 2019-06-18 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='PdtImg',
            new_name='Img',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Pdtdesc',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Pdtname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Pdtprice',
            new_name='price',
        ),
    ]
