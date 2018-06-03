# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('telephone', models.CharField(verbose_name='联系电话', max_length=15)),
                ('address', models.CharField(verbose_name='联系地址', max_length=15)),
                ('person', models.CharField(verbose_name='联系人', max_length=15)),
            ],
            options={
                'verbose_name': '联系方式',
                'verbose_name_plural': '联系方式',
            },
        ),
    ]
