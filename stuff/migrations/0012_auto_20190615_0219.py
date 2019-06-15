# Generated by Django 2.2 on 2019-06-15 01:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0011_auto_20190615_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logreport',
            name='report_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 15, 2, 19, 53, 274595)),
        ),
        migrations.AlterField(
            model_name='logreport',
            name='subject_name',
            field=models.CharField(help_text='Who, if anyone, is this report about?', max_length=100),
        ),
    ]