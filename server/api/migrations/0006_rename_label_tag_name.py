# Generated by Django 4.1.3 on 2023-02-28 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_product_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='label',
            new_name='name',
        ),
    ]
