# Generated by Django 4.2.4 on 2023-09-03 08:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0004_alter_operation_op_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='op_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='operation date'),
        ),
    ]
