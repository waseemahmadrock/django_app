# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-06-20 13:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fOn', '0010_auto_20170620_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='usercomment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]