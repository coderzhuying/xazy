# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import system.storage


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='标题', max_length=40)),
                ('content', models.TextField(verbose_name='内容')),
                ('pub_date', models.DateTimeField(verbose_name='发布时间', auto_now=True)),
                ('author', models.CharField(verbose_name='发布人', max_length=20)),
                ('img', models.ImageField(verbose_name='图片', null=True, upload_to='life/', storage=system.storage.ImageStorage())),
            ],
            options={
                'verbose_name': '业主之家',
                'verbose_name_plural': '业主之家',
            },
        ),
    ]
