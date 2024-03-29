# Generated by Django 2.2.3 on 2020-12-02 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producer', '0004_auto_20201202_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producer',
            name='fertilizer',
            field=models.CharField(blank=True, choices=[('natural_en', 'Natural'), ('artificial_en', 'Artificial'), ('natural_ro', 'Naturale'), ('artificial_ro', 'Artificiale')], max_length=13, null=True, verbose_name='Use of fertilizer'),
        ),
        migrations.AlterField(
            model_name='producer',
            name='irrigation_interest',
            field=models.CharField(blank=True, choices=[('yes_en', 'Yes'), ('no_en', 'No'), ('yes_ro', 'Da'), ('no_ro', 'Nu')], max_length=6, null=True, verbose_name='If not, do you have interest?'),
        ),
        migrations.AlterField(
            model_name='producer',
            name='irrigation_quality',
            field=models.CharField(blank=True, choices=[('source_en', 'From source'), ('underground_en', 'Underground water'), ('source_ro', 'Din sursă'), ('underground_ro', 'Apă subterană')], max_length=14, null=True, verbose_name='Water quality'),
        ),
        migrations.AlterField(
            model_name='producer',
            name='irrigation_use',
            field=models.CharField(blank=True, choices=[('yes_en', 'Yes'), ('no_en', 'No'), ('yes_ro', 'Da'), ('no_ro', 'Nu')], max_length=6, null=True, verbose_name='Do you use water for irrigation?'),
        ),
        migrations.AlterField(
            model_name='producer',
            name='type',
            field=models.CharField(blank=True, choices=[('certificate_en', 'Certificate of producer'), ('small_company_en', 'Small company'), ('small_gardening_en', 'Small gardening'), ('certificate_ro', 'Deținător de certificat de producător'), ('small_company_ro', 'Companie mică'), ('small_gardening_ro', 'Producător local')], max_length=18, null=True, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='producer',
            name='use',
            field=models.CharField(blank=True, choices=[('homefood_en', 'Homefood'), ('other_en', 'Other'), ('homefood_ro', 'Uz casnic'), ('other_ro', 'Alte utilizări alimentare')], max_length=11, null=True, verbose_name='Uses'),
        ),
    ]
