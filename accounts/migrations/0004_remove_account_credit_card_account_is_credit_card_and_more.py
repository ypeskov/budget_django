# Generated by Django 4.2.4 on 2023-09-02 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_credit_card'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='credit_card',
        ),
        migrations.AddField(
            model_name='account',
            name='is_credit_card',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='account',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='credit_card', to='accounts.account'),
        ),
    ]