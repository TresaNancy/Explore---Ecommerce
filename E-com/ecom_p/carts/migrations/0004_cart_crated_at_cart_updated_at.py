# Generated by Django 4.2.3 on 2023-08-10 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_cart_user_cartitem_variant'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='crated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]