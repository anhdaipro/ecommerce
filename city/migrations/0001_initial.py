# Generated by Django 3.2.4 on 2022-04-09 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maqh', models.CharField(max_length=10, null=True)),
                ('matp', models.CharField(max_length=10, null=True)),
                ('name', models.CharField(max_length=100)),
                ('level', models.IntegerField()),
            ],
        ),
    ]
