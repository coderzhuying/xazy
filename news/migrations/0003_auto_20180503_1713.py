# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20180425_1659'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companynews',
            options={'verbose_name': '公司新闻', 'verbose_name_plural': '公司新闻'},
        ),
        migrations.AlterModelOptions(
            name='localnews',
            options={'verbose_name': '地方动态', 'verbose_name_plural': '地方动态'},
        ),
        migrations.AlterModelOptions(
            name='medianews',
            options={'verbose_name': '媒体新闻', 'verbose_name_plural': '媒体新闻'},
        ),
        migrations.AlterField(
            model_name='companynews',
            name='author',
            field=models.CharField(verbose_name='发布人', max_length=20),
        ),
        migrations.AlterField(
            model_name='companynews',
            name='content',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='companynews',
            name='pub_date',
            field=models.DateTimeField(verbose_name='发布时间', auto_now=True),
        ),
        migrations.AlterField(
            model_name='companynews',
            name='title',
            field=models.CharField(verbose_name='标题', max_length=40),
        ),
        migrations.AlterField(
            model_name='localnews',
            name='author',
            field=models.CharField(verbose_name='发布人', max_length=20),
        ),
        migrations.AlterField(
            model_name='localnews',
            name='content',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='localnews',
            name='pub_date',
            field=models.DateTimeField(verbose_name='发布时间', auto_now=True),
        ),
        migrations.AlterField(
            model_name='localnews',
            name='title',
            field=models.CharField(verbose_name='标题', max_length=40),
        ),
        migrations.AlterField(
            model_name='medianews',
            name='author',
            field=models.CharField(verbose_name='发布人', max_length=20),
        ),
        migrations.AlterField(
            model_name='medianews',
            name='content',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='medianews',
            name='pub_date',
            field=models.DateTimeField(verbose_name='发布时间', auto_now=True),
        ),
        migrations.AlterField(
            model_name='medianews',
            name='title',
            field=models.CharField(verbose_name='标题', max_length=40),
        ),
    ]
