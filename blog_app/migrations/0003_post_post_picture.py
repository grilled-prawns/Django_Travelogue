# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-21 15:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_auto_20171207_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_picture',
            field=models.FileField(default=django.utils.timezone.now, upload_to=b''),
            preserve_default=False,
        ),
    ]