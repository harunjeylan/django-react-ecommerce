# Generated by Django 4.1.3 on 2023-02-28 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('code', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product-images')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
                ('collection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.collection')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='product-images')),
                ('images', models.ManyToManyField(blank=True, to='api.image')),
                ('organize', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.organize')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('options', models.ManyToManyField(to='api.option')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('products', models.ManyToManyField(to='api.product')),
            ],
        ),
        migrations.CreateModel(
            name='VariantOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.option')),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.variant')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='variants',
            field=models.ManyToManyField(to='api.variantoption'),
        ),
        migrations.AddField(
            model_name='organize',
            name='tags',
            field=models.ManyToManyField(to='api.tag'),
        ),
        migrations.AddField(
            model_name='organize',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.vendor'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('email', models.EmailField(max_length=254)),
                ('fulfillment_status', models.CharField(choices=[('complete', 'Complete'), ('failed', 'Failed'), ('cancelled', 'Cancelled'), ('complete', 'Complete'), ('pending', 'Pending'), ('partially_fulfilled', 'Partially Fulfilled')], default='pending', max_length=25)),
                ('delivery_type', models.CharField(choices=[('worldwide_delivery', 'Worldwide Delivery'), ('selected_countries', 'Selected Countries'), ('local_delivery', 'Local Delivery')], default='local_delivery', max_length=25)),
                ('countries', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.countries')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('products', models.ManyToManyField(blank=True, to='api.product')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regular_pricing', models.FloatField()),
                ('sale_pricing', models.FloatField()),
                ('stock', models.FloatField()),
                ('shipping_type', models.CharField(choices=[('fulfilled_by_seller', 'Fulfilled by Seller'), ('fulfilled_by_phoenix', 'Fulfilled by Phoenix')], default='fulfilled_by_seller', max_length=25)),
                ('global_delivery', models.CharField(choices=[('worldwide_delivery', 'Worldwide Delivery'), ('selected_countries', 'Selected Countries'), ('local_delivery', 'Local Delivery')], default='worldwide_delivery', max_length=25)),
                ('fragile_product', models.BooleanField(blank=True, default=False)),
                ('biodegradable', models.BooleanField(blank=True, default=False)),
                ('frozen_product', models.BooleanField(blank=True, default=False)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('countries', models.ManyToManyField(to='api.countries')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
            ],
        ),
    ]
