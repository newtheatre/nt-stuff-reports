# Generated by Django 2.2 on 2019-06-10 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0002_auto_20190610_1403'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='show',
            options={'ordering': ['-performance_start', 'show_date']},
        ),
    ]
