# Generated by Django 2.2.13 on 2020-06-15 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsettings', '0002_auto_20200527_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appsettings',
            name='choices',
            field=models.CharField(max_length=70, verbose_name='choices'),
        ),
        migrations.AlterField(
            model_name='appsettings',
            name='description',
            field=models.CharField(max_length=100, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='appsettings',
            name='key',
            field=models.CharField(db_index=True, max_length=50, unique=True, verbose_name='key'),
        ),
        migrations.AlterField(
            model_name='appsettings',
            name='name',
            field=models.CharField(max_length=25, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='appsettings',
            name='value',
            field=models.CharField(max_length=25, verbose_name='value'),
        ),
    ]
