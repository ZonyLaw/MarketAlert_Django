# Generated by Django 4.1.7 on 2023-04-10 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketApi', '0002_trade_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='end_date',
            field=models.DateField(auto_now=True),
        ),
    ]
