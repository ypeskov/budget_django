# Generated by Django 4.2.4 on 2023-09-01 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(db_comment='3 symbols comments', max_length=3, unique=True)),
                ('name', models.CharField(db_comment='English name of the currency', max_length=50)),
                ('symbol', models.CharField(blank=True, db_comment='symbol of currency', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
