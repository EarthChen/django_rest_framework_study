# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-08 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentSorce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField()),
                ('math', models.FloatField()),
                ('english', models.FloatField()),
                ('chiness', models.FloatField()),
            ],
        ),
    ]