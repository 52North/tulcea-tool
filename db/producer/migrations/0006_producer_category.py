# Generated by Django 2.2.3 on 2021-06-10 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producer', '0005_auto_20201202_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='producer',
            name='category',
            field=models.CharField(blank=True, choices=[('dairy_products_en', 'Dairy products'), ('fruits_en', 'Fruits'), ('vegetables_en', 'Vegetables'), ('meat_en', 'Meat'), ('fish_en', 'Fish'), ('bakery_products_en', 'Bakery products'), ('honey_en', 'Honey'), ('dairy_products_ro', 'Lactate'), ('fruits_ro', 'Fructe'), ('vegetables_ro', 'Legume'), ('meat_ro', 'Carne'), ('fish_ro', 'Peste'), ('bakery_products_ro', 'Produse panificatie'), ('honey_ro', 'Miere')], max_length=18, null=True, verbose_name='Category'),
        ),
    ]