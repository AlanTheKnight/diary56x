# Generated by Django 3.2.13 on 2022-04-22 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220422_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plugin',
            name='month_price',
        ),
    ]