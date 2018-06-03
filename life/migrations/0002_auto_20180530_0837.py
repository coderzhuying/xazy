# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import system.storage


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='img',
            field=models.ImageField(verbose_name='图片', blank=True, null=True, upload_to='life/', storage=system.storage.ImageStorage()),
        ),
    ]
