# Generated by Django 4.1.3 on 2023-03-09 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_remove_variantoption_option_variantoption_option'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variantoption',
            old_name='option',
            new_name='options',
        ),
    ]
