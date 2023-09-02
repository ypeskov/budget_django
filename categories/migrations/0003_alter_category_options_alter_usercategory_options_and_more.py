# Generated by Django 4.2.4 on 2023-09-02 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_alter_category_parent_alter_usercategory_parent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='usercategory',
            options={'verbose_name': 'user category', 'verbose_name_plural': 'user categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='categories.category', verbose_name='parent'),
        ),
        migrations.AlterField(
            model_name='category',
            name='type',
            field=models.CharField(choices=[('income', 'Income'), ('expense', 'Expense')], max_length=10),
        ),
    ]
