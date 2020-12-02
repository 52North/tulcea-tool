# Generated by Django 2.2.3 on 2020-12-02 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storagepoint', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storagepoint',
            name='toggle',
            field=models.CharField(blank=True, choices=[('gps', 'Folosește GPS / Use GPS'), ('interactive', 'Punct pe hartă / Point on Map'), ('manual', 'Introducere manuală / Enter Manually')], max_length=11, null=True, verbose_name='Location Mode'),
        ),
    ]