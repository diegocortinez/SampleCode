# Generated by Django 4.1 on 2022-08-08 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Savings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savings',
            name='savings_balance',
            field=models.BigIntegerField(),
        ),
    ]
