# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landlords', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=255)),
                ('tenant', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('date_time', models.DateTimeField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['rent']},
        ),
        migrations.AlterField(
            model_name='landlord',
            name='email',
            field=models.EmailField(max_length=255),
        ),
        migrations.AddField(
            model_name='message',
            name='landlord',
            field=models.ForeignKey(to='landlords.Landlord'),
        ),
    ]
