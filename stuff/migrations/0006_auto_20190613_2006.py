# Generated by Django 2.2 on 2019-06-13 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0005_auto_20190610_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venuereport',
            name='notes',
        ),
        migrations.AddField(
            model_name='venuereport',
            name='venue_notes',
            field=models.TextField(blank=True, help_text='General notes', null=True),
        ),
    ]
