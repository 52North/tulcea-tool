# Generated by Django 2.2.3 on 2020-12-02 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energyusage', '0002_auto_20201202_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energyusage',
            name='energy_type',
            field=models.CharField(blank=True, choices=[('national_en', 'National system'), ('renewable_en', 'Renewable'), ('both_en', 'Both'), ('national_ro', 'Sistem Național'), ('renewable_ro', 'Regenerabilă'), ('both_ro', 'Amândouă')], max_length=12, null=True, verbose_name='What type of energy do you use?'),
        ),
        migrations.AlterField(
            model_name='energyusage',
            name='more_renewable',
            field=models.CharField(blank=True, choices=[('yes_en', 'Yes'), ('no_en', 'No'), ('yes_ro', 'Da'), ('no_ro', 'Nu')], max_length=6, null=True, verbose_name='Would you like to use more renewable energy?'),
        ),
        migrations.AlterField(
            model_name='energyusage',
            name='renewable_type',
            field=models.CharField(blank=True, choices=[('solar_en', 'Solar'), ('wind_en', 'Wind'), ('water_en', 'Water'), ('geothermal_en', 'Geothermal'), ('bio_en', 'Bio'), ('other_en', 'Other'), ('solar_ro', 'Solar'), ('wind_ro', 'Vânt'), ('water_ro', 'Apă'), ('geothermal_ro', 'Geotermală'), ('bio_ro', 'Bio'), ('other_ro', 'Alte')], max_length=13, null=True, verbose_name='What type of renewable energy do you use?'),
        ),
    ]
