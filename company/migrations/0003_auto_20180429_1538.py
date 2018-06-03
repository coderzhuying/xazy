# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_companystructure'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyculture',
            name='img',
        ),
        migrations.RemoveField(
            model_name='companyprofile',
            name='img',
        ),
    ]
