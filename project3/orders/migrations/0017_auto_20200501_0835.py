# Generated by Django 2.0.3 on 2020-05-01 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_toppings_addition'),
    ]

    operations = [
        migrations.CreateModel(
            name='Additions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(max_length=64)),
            ],
        ),
        migrations.RemoveField(
            model_name='toppings',
            name='addition',
        ),
    ]
