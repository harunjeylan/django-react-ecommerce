# Generated by Django 4.1.3 on 2023-02-28 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_product_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Countries',
            new_name='Country',
        ),
        migrations.AddField(
            model_name='inventory',
            name='max_allowed_temperature',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
