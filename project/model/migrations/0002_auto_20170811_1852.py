# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id1', models.CharField(max_length=20)),
                ('id2', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('lessons', models.ManyToManyField(to='model.Lesson')),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]