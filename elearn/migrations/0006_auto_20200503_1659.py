# Generated by Django 3.0.3 on 2020-05-03 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearn', '0005_auto_20200503_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registered_course',
            name='reg_unit',
            field=models.IntegerField(),
        ),
    ]
