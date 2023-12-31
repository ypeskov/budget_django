# Generated by Django 4.2.4 on 2023-09-03 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0005_alter_exchangeratecurrent_options_and_more'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='base_currency',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='currencies.currency'),
            preserve_default=False,
        ),
    ]
