# Generated by Django 3.2.10 on 2021-12-24 11:06

import apps.authentication.manager
import apps.authentication.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('account_type', models.IntegerField(choices=[(0, 'Root'), (1, 'Администратор'), (2, 'Учитель'), (3, 'Ученик')], default=apps.authentication.utils.UserTypes['STUDENT'], verbose_name='Тип аккаунта')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Администратор')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('second_name', models.CharField(blank=True, default='', max_length=100, verbose_name='Отчество')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('registration_date', models.DateField(auto_now_add=True, null=True, verbose_name='Дата регистрации')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'permissions': [('edit_news', 'Может редактировать статьи в новостном блоке.')],
            },
            managers=[
                ('objects', apps.authentication.manager.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='options_admin', serialize=False, to='authentication.user', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Параметры администратора',
                'verbose_name_plural': 'Параметры администраторов',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='options_student', serialize=False, to='authentication.user', verbose_name='Пользователь')),
                ('is_monitor', models.BooleanField(default=False, verbose_name='Староста')),
            ],
            options={
                'verbose_name': 'Ученик',
                'verbose_name_plural': 'Ученики',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='options_teacher', serialize=False, to='authentication.user', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Учитель',
                'verbose_name_plural': 'Учителя',
            },
        ),
    ]