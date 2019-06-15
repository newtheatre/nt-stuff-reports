# Generated by Django 2.2 on 2019-06-14 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0008_auto_20190615_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logreport',
            name='company_name',
            field=models.ForeignKey(blank=True, default=None, help_text='If this log entry is to do with a company, select which one.', on_delete=django.db.models.deletion.CASCADE, to='stuff.Company'),
        ),
        migrations.AlterField(
            model_name='logreport',
            name='show_name',
            field=models.ForeignKey(blank=True, default=None, help_text='If this log entry is to do with a show, select which one.', on_delete=django.db.models.deletion.CASCADE, to='stuff.Show'),
        ),
    ]
