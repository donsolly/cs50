# Generated by Django 3.0.3 on 2020-05-03 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearn', '0011_auto_20200503_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='receiver',
            field=models.CharField(default='don', max_length=50),
            preserve_default=False,
        ),
    ]
