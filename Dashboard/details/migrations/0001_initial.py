# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('name', models.CharField(max_length=250, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('enquiry_type', models.CharField(max_length=250, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('status_info', models.CharField(max_length=250, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250, serialize=False, primary_key=True)),
                ('doj', models.DateField()),
                ('course', models.ForeignKey(to='details.Course')),
                ('enquiry', models.ForeignKey(to='details.Enquiry')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
