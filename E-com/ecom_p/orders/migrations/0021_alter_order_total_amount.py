# Generated by Django 4.2.3 on 2023-09-01 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_alter_order_address_line_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_amount',
            field=models.IntegerField(default=0),
        ),
    ]
