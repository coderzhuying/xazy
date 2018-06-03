# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20180503_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='companynews',
            name='img',
            field=models.ImageField(verbose_name='图片', blank=True, null=True, upload_to='company/'),
        ),
        migrations.AddField(
            model_name='localnews',
            name='img',
            field=models.ImageField(verbose_name='图片', blank=True, null=True, upload_to='local/'),
        ),
        migrations.AddField(
            model_name='medianews',
            name='img',
            field=models.ImageField(verbose_name='图片', blank=True, null=True, upload_to='media/'),
        ),
    ]
