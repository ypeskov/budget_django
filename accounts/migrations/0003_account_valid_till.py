# Generated by Django 4.2.4 on 2023-09-02 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_account_valid_till'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='valid_till',
            field=models.DateField(blank=True, null=True),
        ),
    ]