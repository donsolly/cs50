# Generated by Django 3.0.3 on 2020-05-03 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearn', '0008_auto_20200503_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='registered_course',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
