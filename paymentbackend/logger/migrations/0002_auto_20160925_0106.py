# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 01:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='commission',
            new_name='transaction_fee',
        ),
    ]
