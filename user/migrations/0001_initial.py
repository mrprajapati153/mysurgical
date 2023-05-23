# Generated by Django 4.1.7 on 2023-05-17 07:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_address', models.CharField(max_length=100)),
                ('shop_city', models.CharField(max_length=50)),
                ('shop_state', models.CharField(max_length=50)),
                ('shop_country', models.CharField(max_length=50)),
                ('shop_pincode', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999999)])),
                ('shop_mobile', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('shop_Background_photo', models.ImageField(upload_to='shop_picture/')),
                ('shop_otherphoto', models.ImageField(upload_to='shop_picture/')),
                ('shop_pancardno', models.CharField(max_length=10)),
                ('shop_GST', models.CharField(max_length=50)),
                ('shop_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_image1', models.ImageField(upload_to='product_picture/')),
                ('product_image2', models.ImageField(upload_to='product_picture/')),
                ('product_manufeacture', models.CharField(max_length=100)),
                ('product_modelno', models.PositiveBigIntegerField(validators=[django.core.validators.MaxValueValidator(111111111111)])),
                ('prodect_detail', models.CharField(max_length=100)),
                ('product_type', models.CharField(max_length=50)),
                ('product_price', models.FloatField(max_length=10)),
                ('shop_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]