# Generated by Django 4.2.4 on 2023-09-03 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0002_exchangeratecurrent_exchangeratehistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangeratecurrent',
            name='rate',
            field=models.DecimalField(decimal_places=6, max_digits=16),
        ),
    ]