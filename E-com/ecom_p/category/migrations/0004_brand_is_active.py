# Generated by Django 4.2.3 on 2023-08-30 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_delete_variant'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]