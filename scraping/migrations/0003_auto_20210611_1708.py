# Generated by Django 3.2 on 2021-06-11 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0002_auto_20210607_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dcdata',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='livenews',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mainnews',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]