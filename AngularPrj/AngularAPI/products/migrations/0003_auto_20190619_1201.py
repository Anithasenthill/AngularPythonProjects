# Generated by Django 2.2.1 on 2019-06-19 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190618_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Img',
            new_name='img',
        ),
    ]
