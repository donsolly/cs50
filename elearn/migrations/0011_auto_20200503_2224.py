# Generated by Django 3.0.3 on 2020-05-03 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearn', '0010_broadcast_personal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registered_course',
            name='paid',
        ),
        migrations.AddField(
            model_name='all_students',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
