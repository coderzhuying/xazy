# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import system.storage


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyCulture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('content', models.TextField()),
                ('img', models.ImageField(upload_to='company/culture', storage=system.storage.ImageStorage())),
            ],
        ),
        migrations.CreateModel(
            name='CompanyMemorabilia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('content', models.TextField()),
                ('img', models.ImageField(upload_to='company/profile', storage=system.storage.ImageStorage())),
            ],
        ),
        migrations.CreateModel(
            name='CompanyTeam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('content1', models.TextField()),
                ('img1', models.ImageField(upload_to='company/team1', storage=system.storage.ImageStorage())),
                ('content2', models.TextField()),
                ('img2', models.ImageField(upload_to='company/team2', storage=system.storage.ImageStorage())),
                ('content3', models.TextField()),
                ('img3', models.ImageField(upload_to='company/team3', storage=system.storage.ImageStorage())),
            ],
        ),
    ]
