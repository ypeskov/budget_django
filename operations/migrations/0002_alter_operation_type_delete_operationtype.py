# Generated by Django 4.2.4 on 2023-09-03 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='type',
            field=models.CharField(choices=[('EXPENSE', 'expense'), ('INCOME', 'income'), ('TRANSFER', 'transfer')], default='EXPENSE', max_length=20),
        ),
        migrations.DeleteModel(
            name='OperationType',
        ),
    ]
