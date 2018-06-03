# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0002_auto_20180530_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='img',
            field=models.ImageField(verbose_name='图片', blank=True, null=True, upload_to='life'),
        ),
    ]
