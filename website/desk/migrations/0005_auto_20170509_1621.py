# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-09 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desk', '0004_auto_20170509_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='img',
        ),
        migrations.AddField(
            model_name='course',
            name='file',
            field=models.FileField(blank=True, upload_to=b''),
        ),
    ]
