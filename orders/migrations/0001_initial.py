# Generated by Django 3.2.4 on 2022-12-22 07:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shipping', '0001_initial'),
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('discounts', '0001_initial'),
        ('carts', '0001_initial'),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('ref_code', models.CharField(max_length=20)),
                ('payment_number', models.CharField(max_length=20, null=True)),
                ('payment_choice', models.CharField(choices=[('PayPal', 'PayPal'), ('Payment on delivery', 'Payment on delivery')], default='After', max_length=20)),
                ('ordered_date', models.DateTimeField()),
                ('accepted_date', models.DateTimeField(null=True)),
                ('received_date', models.DateTimeField(null=True)),
                ('canceled_date', models.DateTimeField(null=True)),
                ('shipping_start_date', models.DateTimeField(null=True)),
                ('being_delivered', models.BooleanField(default=False)),
                ('accepted', models.BooleanField(default=False)),
                ('received', models.BooleanField(default=False)),
                ('refund_requested', models.BooleanField(default=False)),
                ('refund_granted', models.BooleanField(default=False)),
                ('canceled', models.BooleanField(default=False)),
                ('amount', models.FloatField(default=0)),
                ('discount_voucher', models.FloatField(default=0, null=True)),
                ('discount_offer', models.FloatField(default=0, null=True)),
                ('award', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_voucher', to='discounts.award')),
                ('follower_offer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_voucher', to='discounts.follower_offer')),
                ('items', models.ManyToManyField(related_name='order_cartitem', to='carts.CartItem')),
                ('shipping', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_shipping', to='shipping.shipping')),
                ('shipping_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_address', to='account.address')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_shop', to='shop.shop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('voucher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_voucher', to='discounts.voucher')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('payment_number', models.CharField(max_length=30)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('paid', models.BooleanField(default=False)),
                ('payment_method', models.CharField(choices=[('P', 'PayPal')], default='P', max_length=10)),
                ('order', models.ManyToManyField(blank=True, to='orders.Order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
