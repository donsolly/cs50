# Generated by Django 2.0.3 on 2020-04-30 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200429_2046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=64)),
                ('main', models.CharField(max_length=64)),
                ('topping', models.CharField(max_length=64, null=True)),
                ('size', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
    ]