# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-08 15:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cvjd', '0005_auto_20190408_1456'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='top_10_keywords',
            new_name='top_keywords',
        ),
    ]