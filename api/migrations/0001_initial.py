# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-08-25 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_code', models.CharField(help_text='社員番号', max_length=10, verbose_name='社員番号')),
                ('emp_name', models.CharField(help_text='メールアドレス', max_length=250, verbose_name='メールアドレス')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]