# Generated by Django 4.1.7 on 2023-05-17 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='contact',
            field=models.IntegerField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
