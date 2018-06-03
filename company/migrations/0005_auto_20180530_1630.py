# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20180503_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyteam',
            name='content1',
        ),
        migrations.RemoveField(
            model_name='companyteam',
            name='content2',
        ),
        migrations.RemoveField(
            model_name='companyteam',
            name='content3',
        ),
        migrations.RemoveField(
            model_name='companyteam',
            name='img1',
        ),
        migrations.RemoveField(
            model_name='companyteam',
            name='img2',
        ),
        migrations.RemoveField(
            model_name='companyteam',
            name='img3',
        ),
        migrations.AddField(
            model_name='companyteam',
            name='content',
            field=models.TextField(verbose_name='内容', default='abc'),
        ),
    ]
