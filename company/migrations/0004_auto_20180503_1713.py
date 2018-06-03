# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import system.storage


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20180429_1538'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companyculture',
            options={'verbose_name': '企业文化', 'verbose_name_plural': '企业文化'},
        ),
        migrations.AlterModelOptions(
            name='companymemorabilia',
            options={'verbose_name': '大事迹', 'verbose_name_plural': '大事迹'},
        ),
        migrations.AlterModelOptions(
            name='companyprofile',
            options={'verbose_name': '公司简介', 'verbose_name_plural': '公司简介'},
        ),
        migrations.AlterModelOptions(
            name='companystructure',
            options={'verbose_name': '组织架构', 'verbose_name_plural': '组织架构'},
        ),
        migrations.AlterModelOptions(
            name='companyteam',
            options={'verbose_name': '团队建设', 'verbose_name_plural': '团队建设'},
        ),
        migrations.AlterField(
            model_name='companyculture',
            name='content',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='companymemorabilia',
            name='content',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='content',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='companystructure',
            name='content',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='companyteam',
            name='content1',
            field=models.TextField(verbose_name='内容1'),
        ),
        migrations.AlterField(
            model_name='companyteam',
            name='content2',
            field=models.TextField(verbose_name='内容2'),
        ),
        migrations.AlterField(
            model_name='companyteam',
            name='content3',
            field=models.TextField(verbose_name='内容3'),
        ),
        migrations.AlterField(
            model_name='companyteam',
            name='img1',
            field=models.ImageField(verbose_name='图片1', upload_to='company/team1', storage=system.storage.ImageStorage()),
        ),
        migrations.AlterField(
            model_name='companyteam',
            name='img2',
            field=models.ImageField(verbose_name='图片2', upload_to='company/team2', storage=system.storage.ImageStorage()),
        ),
        migrations.AlterField(
            model_name='companyteam',
            name='img3',
            field=models.ImageField(verbose_name='图片3', upload_to='company/team3', storage=system.storage.ImageStorage()),
        ),
    ]
