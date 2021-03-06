# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-07 16:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('etherpad', '0007_auto_20180607_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='padgroup',
            name='group',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='padgroup',
            name='server',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='etherpad.PadServer'),
        ),
    ]
