# Generated by Django 2.0.3 on 2020-04-30 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_cart_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.CharField(max_length=64),
        ),
    ]