# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-08-25 08:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default=django.utils.timezone.now, help_text='メールアドレス', max_length=250, verbose_name='メールアドレス'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='emp_name',
            field=models.CharField(help_text='社員名', max_length=150, verbose_name='社員名'),
        ),
    ]