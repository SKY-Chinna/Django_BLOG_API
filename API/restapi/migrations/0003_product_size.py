# Generated by Django 4.1 on 2022-08-26 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0002_product_shirt_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.IntegerField(default=False),
        ),
    ]
