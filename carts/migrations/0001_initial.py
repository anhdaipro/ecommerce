# Generated by Django 3.2.4 on 2022-12-22 07:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('discounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhishItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.SmallIntegerField(default=1)),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='whish_item', to='shop.item')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='whish_product', to='shop.variation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.SmallIntegerField()),
                ('amount_main_products', models.FloatField(default=0, null=True)),
                ('amount_byproducts', models.FloatField(default=0, null=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('ordered', models.BooleanField(default=False)),
                ('check', models.BooleanField(default=False)),
                ('deal_shock', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='discounts.buy_with_shock_deal')),
                ('flash_sale', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='discounts.flash_sale')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_item', to='shop.item')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_product', to='shop.variation')),
                ('program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='discounts.shop_program')),
                ('promotion_combo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='discounts.promotion_combo')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_order', to='shop.shop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Byproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('updated_at', models.DateField(auto_now=True)),
                ('cartitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='byproduct_cart', to='carts.cartitem')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='byproduct_item', to='shop.item')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='byproduct_product', to='shop.variation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
