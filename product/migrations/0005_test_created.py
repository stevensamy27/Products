# Generated by Django 3.2.8 on 2022-01-29 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_test_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='created',
            field=models.DateTimeField(null=True),
        ),
    ]
