# Generated by Django 3.1.1 on 2020-09-29 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDDiscountPrice',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5, verbose_name='Discount Price'),
            preserve_default=False,
        ),
    ]
