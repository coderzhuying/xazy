# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import system.storage


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BigImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('bigimg1', models.ImageField(upload_to='index/bigimg1', storage=system.storage.ImageStorage())),
                ('bigimg2', models.ImageField(upload_to='index/bigimg2', storage=system.storage.ImageStorage())),
                ('bigimg3', models.ImageField(upload_to='index/bigimg3', storage=system.storage.ImageStorage())),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=40)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SamllImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('samllimg1', models.ImageField(upload_to='index/samllimg1', storage=system.storage.ImageStorage())),
                ('samllimg2', models.ImageField(upload_to='index/samllimg2', storage=system.storage.ImageStorage())),
                ('samllimg3', models.ImageField(upload_to='index/samllimg3', storage=system.storage.ImageStorage())),
                ('samllimg4', models.ImageField(upload_to='index/samllimg4', storage=system.storage.ImageStorage())),
                ('samllimg5', models.ImageField(upload_to='index/samllimg5', storage=system.storage.ImageStorage())),
                ('samllimg6', models.ImageField(upload_to='index/samllimg6', storage=system.storage.ImageStorage())),
            ],
        ),
    ]
