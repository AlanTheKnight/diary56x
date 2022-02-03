# Generated by Django 3.2.10 on 2022-01-30 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_auto_20220130_2257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n', models.IntegerField(verbose_name='Номер урока')),
                ('start', models.TimeField(verbose_name='Начало урока')),
                ('end', models.TimeField(verbose_name='Конец урока')),
            ],
            options={
                'verbose_name': 'Звонок',
                'verbose_name_plural': 'Звонки',
                'ordering': ['timetable', 'n'],
            },
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.school')),
            ],
            options={
                'verbose_name': 'TimeTable',
                'verbose_name_plural': 'TimeTables',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday')], verbose_name='День недели')),
                ('classroom', models.CharField(max_length=50, verbose_name='Кабинет')),
                ('klass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='core.klass', verbose_name='Класс')),
                ('number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.bell', verbose_name='Номер урока')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subject', verbose_name='Предмет')),
            ],
        ),
        migrations.AddField(
            model_name='bell',
            name='timetable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.timetable'),
        ),
    ]