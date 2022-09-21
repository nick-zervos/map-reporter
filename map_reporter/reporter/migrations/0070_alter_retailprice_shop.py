# Generated by Django 4.1 on 2022-09-21 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reporter", "0069_alter_retailprice_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="retailprice",
            name="shop",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="reporter.shop",
            ),
        ),
    ]
