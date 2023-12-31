# Generated by Django 3.2.4 on 2022-12-22 07:55

import cloudinary_storage.storage
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myweb', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shipping', '0001_initial'),
        
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('value', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='color/')),
            ],
        ),
        migrations.CreateModel(
            name='IpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
                ('create_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('brand', models.TextField(max_length=200)),
                ('description', models.TextField(max_length=3000)),
                ('sku_product', models.CharField(max_length=20, null=True)),
                ('status', models.CharField(choices=[('1', 'New'), ('2', 'Like New')], default='1', max_length=20)),
                ('pre_order', models.CharField(max_length=20, null=True)),
                ('weight', models.IntegerField(null=True)),
                ('height', models.IntegerField(null=True)),
                ('width', models.IntegerField(null=True)),
                ('length', models.IntegerField(null=True)),
                ('price_ship', models.FloatField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('views', models.IntegerField(default=0)),
                ('slug', models.SlugField(max_length=150, null=True)),
                ('violet', models.BooleanField(default=False)),
                ('hidden', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now=True)),
                ('detail', models.JSONField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('shop_type', models.CharField(choices=[('Mall', 'Shopmall'), ('Favourite', 'Favourite')], max_length=25, null=True)),
                ('views', models.IntegerField(default=0)),
                ('slug', models.SlugField(null=True)),
                ('image_cover', models.ImageField(null=True, upload_to='shop/')),
                ('city', models.CharField(max_length=200, null=True)),
                ('description_url', models.ManyToManyField(blank=True, to='myweb.Image_home')),
                ('shipping', models.ManyToManyField(blank=True, to='shipping.Shipping')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='shop', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('value', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('price', models.IntegerField()),
                ('inventory', models.IntegerField()),
                ('sku_classify', models.CharField(max_length=20, null=True)),
                ('view', models.IntegerField(default=0)),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.color')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variation_item', to='shop.item')),
                ('size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.size')),
            ],
            options={
                'ordering': ['color'],
            },
        ),
        migrations.CreateModel(
            name='UploadItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='item/')),
                ('image_preview', models.FileField(null=True, storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='item/')),
                ('duration', models.FloatField(null=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('upload_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shop')),
            ],
        ),
        migrations.CreateModel(
            name='ShopViews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_views', to='shop.shop')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Liker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_likers', to='shop.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItemViews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_views', to='shop.item')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='media_upload',
            field=models.ManyToManyField(blank=True, related_name='media_upload', to='shop.UploadItem'),
        ),
        migrations.AddField(
            model_name='item',
            name='shipping_choice',
            field=models.ManyToManyField(blank=True, related_name='shipping_choice', to='shipping.Shipping'),
        ),
        migrations.AddField(
            model_name='item',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shop'),
        ),
        migrations.CreateModel(
            name='BuyMoreDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_quantity', models.IntegerField()),
                ('to_quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buymore_item', to='shop.item')),
            ],
        ),
    ]
