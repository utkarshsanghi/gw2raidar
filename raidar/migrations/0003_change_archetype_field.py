# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-12 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raidar', '0002_populate_areas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participation',
            name='archetype',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Power'), (2, 'Condi'), (3, 'Tank'), (4, 'Heal'), (5, 'Support')], db_index=True),
        ),
    ]
