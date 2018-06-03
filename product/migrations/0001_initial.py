# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('content', models.TextField(verbose_name='内容')),
                ('tel', models.CharField(verbose_name='联系电话', max_length=15)),
            ],
            options={
                'verbose_name': '汽车维修',
                'verbose_name_plural': '汽车维修',
            },
        ),
        migrations.CreateModel(
            name='Housekeeping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('content', models.TextField(verbose_name='内容')),
                ('tel', models.CharField(verbose_name='联系电话', max_length=15)),
            ],
            options={
                'verbose_name': '家政服务',
                'verbose_name_plural': '家政服务',
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('content', models.TextField(verbose_name='内容')),
                ('tel', models.CharField(verbose_name='联系电话', max_length=15)),
            ],
            options={
                'verbose_name': '便民维修',
                'verbose_name_plural': '便民维修',
            },
        ),
    ]
