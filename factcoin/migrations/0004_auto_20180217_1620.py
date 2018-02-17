# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-17 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factcoin', '0003_remove_document_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='localizations',
            field=models.TextField(max_length=500, null=True, verbose_name='localizations'),
        ),
        migrations.AddField(
            model_name='document',
            name='organizations',
            field=models.TextField(max_length=500, null=True, verbose_name='localizations'),
        ),
        migrations.AddField(
            model_name='document',
            name='people',
            field=models.TextField(max_length=500, null=True, verbose_name='localizations'),
        ),
        migrations.AddField(
            model_name='document',
            name='timestamp',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='authors',
            field=models.CharField(max_length=500, null=True, verbose_name='authors'),
        ),
    ]
