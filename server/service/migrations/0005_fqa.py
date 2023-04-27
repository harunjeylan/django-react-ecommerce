# Generated by Django 4.1.7 on 2023-04-27 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fqa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('answer', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
