# Generated by Django 3.2.4 on 2022-04-09 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='maqh',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='matp',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
