# Generated by Django 4.2.3 on 2023-08-23 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_order_coupon_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='coupon_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
