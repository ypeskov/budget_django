# Generated by Django 4.2.4 on 2023-09-03 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRateCurrent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rate', models.DecimalField(decimal_places=4, max_digits=16)),
                ('bought_currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bought_currency', to='currencies.currency')),
                ('sold_currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sold_currency', to='currencies.currency')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExchangeRateHistory',
            fields=[
                ('exchangeratecurrent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='currencies.exchangeratecurrent')),
                ('rate_date', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
            bases=('currencies.exchangeratecurrent',),
        ),
    ]
