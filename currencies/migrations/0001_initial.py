# Generated by Django 4.2.4 on 2023-09-02 07:46

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
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(db_comment='3 symbols comments', max_length=3, unique=True)),
                ('numeric_code', models.SmallIntegerField(blank=True, null=True, unique=True)),
                ('name', models.CharField(db_comment='English name of the currency', max_length=50)),
                ('symbol', models.CharField(blank=True, db_comment='symbol of currency', max_length=5)),
            ],
            options={
                'verbose_name': 'currency',
                'verbose_name_plural': 'currencies',
            },
        ),
    ]
