# Generated by Django 4.1.7 on 2023-05-02 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_alter_contact_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordereditem',
            name='sale_pricing',
            field=models.FloatField(default=12),
            preserve_default=False,
        ),
    ]
