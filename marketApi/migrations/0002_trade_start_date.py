# Generated by Django 4.1.7 on 2023-04-10 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketApi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='start_date',
            field=models.DateField(default=False),
        ),
    ]
