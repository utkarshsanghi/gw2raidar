# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-12 01:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('raidar', '0003_change_archetype_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portrait_url', models.URLField(null=True)),
                ('stats', models.TextField(default='{}', editable=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
                ('last_notified_at', models.IntegerField(db_index=True, default=0, editable=False)),
            ],
        ),
    ]
