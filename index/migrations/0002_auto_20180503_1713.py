# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import system.storage


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bigimage',
            options={'verbose_name': '封面大图', 'verbose_name_plural': '封面大图'},
        ),
        migrations.AlterModelOptions(
            name='notice',
            options={'verbose_name': '通知公告', 'verbose_name_plural': '通知公告'},
        ),
        migrations.AlterModelOptions(
            name='samllimage',
            options={'verbose_name': '小轮播图', 'verbose_name_plural': '小轮播图'},
        ),
        migrations.AlterField(
            model_name='bigimage',
            name='bigimg1',
            field=models.ImageField(verbose_name='图片1', upload_to='index/bigimg1', storage=system.storage.ImageStorage()),
        ),
        migrations.AlterField(
            model_name='bigimage',
            name='bigimg2',
            field=models.ImageField(verbose_name='图片2', upload_to='index/bigimg2', storage=system.storage.ImageStorage()),
        ),
        migrations.AlterField(
            model_name='bigimage',
            name='bigimg3',
            field=models.ImageField(verbose_name='图片3', upload_to='index/bigimg3', storage=system.storage.ImageStorage()),
        ),
        migrations.AlterField(
            model_name='notice',
            name='content',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='pub_date',
            field=models.DateTimeField(verbose_name='发布时间', auto_now=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='title',
            field=models.CharField(verbose_name='标题', max_length=40),
        ),
        migrations.AlterField(
            model_name='samllimage',
            name='samllimg1',
            field=models.ImageField(verbose_name='图片1', upload_to='index/samllimg1', storage=system.storage.ImageStorage()),
        ),
        migrations.AlterField(
            model_name='samllimage',
            name='samllimg2',
            field=models.ImageField(verbose_name='图片2', upload_to='index/samllimg2', storage=system.storage.ImageStorage()),
        ),
        migrations.AlterField(
            model_name='samllimage',
            name='samllimg3',
            field=models.ImageField(verbose_name='图片3', upload_to='index/samllimg3', storage=system.storage.ImageStorage()),
        ),
        migrations.AlterField(
            model_name='samllimage',
            name='samllimg4',
            field=models.ImageField(verbose_name='图片4', upload_to='index/samllimg4', storage=system.storage.ImageStorage()),
        ),
        migrations.AlterField(
            model_name='samllimage',
            name='samllimg5',
            field=models.ImageField(verbose_name='图片5', upload_to='index/samllimg5', storage=system.storage.ImageStorage()),
        ),
        migrations.AlterField(
            model_name='samllimage',
            name='samllimg6',
            field=models.ImageField(verbose_name='图片6', upload_to='index/samllimg6', storage=system.storage.ImageStorage()),
        ),
    ]
