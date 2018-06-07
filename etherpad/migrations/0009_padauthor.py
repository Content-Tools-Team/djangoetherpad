# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-07 17:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('etherpad', '0008_auto_20180607_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='PadAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorID', models.CharField(blank=True, max_length=256)),
                ('group', models.ManyToManyField(blank=True, related_name='authors', to='etherpad.PadGroup')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etherpad.PadServer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'author',
            },
        ),
    ]
