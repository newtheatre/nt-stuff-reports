# Generated by Django 2.2 on 2019-06-14 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0007_auto_20190614_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='logreport',
            name='company_name',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='stuff.Company'),
        ),
        migrations.AddField(
            model_name='logreport',
            name='show_name',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='stuff.Show'),
        ),
        migrations.AlterField(
            model_name='logreport',
            name='report_type',
            field=models.CharField(choices=[('A', 'Accident'), ('I', 'Incident'), ('C', 'Complaint'), ('N', 'Note')], max_length=50),
        ),
    ]
