# Generated by Django 4.0.4 on 2022-06-16 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0033_shop_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='name',
        ),
    ]
