# Generated by Django 3.2.13 on 2022-06-10 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_klass_subjects'),
        ('timetable', '0004_auto_20220501_1847'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='timetablelesson',
            unique_together={('number', 'day', 'klass', 'subject')},
        ),
        migrations.RemoveField(
            model_name='timetablelesson',
            name='group',
        ),
    ]
