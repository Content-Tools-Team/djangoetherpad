# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-05 19:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etherpad', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pad',
            name='group',
        ),
    ]