# Generated by Django 3.2.4 on 2022-12-22 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=100)),
                ('shipping_unit', models.CharField(max_length=100, null=True)),
                ('tax_code', models.CharField(max_length=100, null=True)),
                ('allowable_volume', models.IntegerField(null=True)),
            ],
        ),
    ]
