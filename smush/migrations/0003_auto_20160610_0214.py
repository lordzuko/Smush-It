# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-10 02:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smush', '0002_document'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='Images',
        ),
    ]
