# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-29 16:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='winning_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='match.Team'),
        ),
    ]
