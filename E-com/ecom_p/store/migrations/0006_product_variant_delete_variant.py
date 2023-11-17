# Generated by Django 4.2.3 on 2023-08-09 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_variant'),
        ('store', '0005_variant_variant_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='variant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='category.variant'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Variant',
        ),
    ]