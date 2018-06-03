# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recruitment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('position', models.CharField(verbose_name='岗位', max_length=40)),
                ('requirements', models.TextField(verbose_name='岗位要求')),
                ('salary', models.CharField(verbose_name='薪资', max_length=40)),
                ('place', models.TextField(verbose_name='工作地')),
            ],
            options={
                'verbose_name': '招聘信息',
                'verbose_name_plural': '招聘信息',
            },
        ),
    ]
