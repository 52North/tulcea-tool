# Generated by Django 2.2.3 on 2020-09-30 12:49

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producer',
            name='geometry_line',
            field=django.contrib.gis.db.models.fields.LineStringField(blank=True, null=True, srid=4326, verbose_name='Use the map to estimate the distance.'),
        ),
        migrations.AlterField(
            model_name='producer',
            name='distance',
            field=models.FloatField(blank=True, null=True, verbose_name='Distance: producer → storage → sale point (km)'),
        ),
    ]