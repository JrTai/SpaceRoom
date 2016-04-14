# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Landlord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=20)),
                ('rent', models.DecimalField(max_digits=3, decimal_places=0)),
                ('postcode', models.CharField(max_length=50, blank=True)),
                ('pet_allowed', models.BooleanField(default=False)),
                ('landlord', models.ForeignKey(to='landlords.Landlord')),
            ],
        ),
    ]
