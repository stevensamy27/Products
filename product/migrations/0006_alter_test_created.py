# Generated by Django 3.2.8 on 2022-01-30 12:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_test_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]