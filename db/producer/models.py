from django.contrib.gis.db import models
import pystache


class Producer(models.Model):
    name = models.TextField(
        null=True,
        blank=True,
        verbose_name="Name",
    )
    type = models.CharField(
        choices=(
            ("certificate_en", "Certificate of producer"),
            ("small_company_en", "Small company"),
            ("small_gardening_en", "Small gardening"),
            ("certificate_ro", "Deținător de certificat de producător"),
            ("small_company_ro", "Companie mică"),
            ("small_gardening_ro", "Producător local"),
        ),
        max_length=18,
        null=True,
        blank=True,
        verbose_name="Type",
    )
    category = models.CharField(
        choices=(
            ("dairy_products_en", "Dairy products"),
            ("fruits_en", "Fruits"),
            ("vegetables_en", "Vegetables"),
            ("meat_en", "Meat"),
            ("fish_en", "Fish"),
            ("bakery_products_en", "Bakery products"),
            ("honey_en", "Honey"),
            ("dairy_products_ro", "Lactate"),
            ("fruits_ro", "Fructe"),
            ("vegetables_ro", "Legume"),
            ("meat_ro", "Carne"),
            ("fish_ro", "Peste"),
            ("bakery_products_ro", "Produse panificatie"),
            ("honey_ro", "Miere"),
        ),
        max_length=18,
        null=True,
        blank=True,
        verbose_name="Category",
    )
    product = models.TextField(
        null=True,
        blank=True,
        verbose_name="Main product(s)",
    )
    address = models.TextField(
        null=True,
        blank=True,
        verbose_name="Address",
    )
    phone = models.TextField(
        null=True,
        blank=True,
        verbose_name="Telephone",
    )
    email = models.TextField(
        null=True,
        blank=True,
        verbose_name="E-mail",
    )
    website = models.TextField(
        null=True,
        blank=True,
        verbose_name="Website",
    )
    toggle = models.CharField(
        choices=(
            ("gps", "Folosește GPS / Use GPS"),
            ("interactive", "Punct pe hartă / Point on Map"),
            ("manual", "Introducere manuală / Enter Manually"),
        ),
        max_length=11,
        null=True,
        blank=True,
        verbose_name="Location Mode",
    )
    geometry = models.PointField(
        srid=4326,
        null=True,
        blank=True,
        verbose_name="Location",
    )
    geometry_line = models.LineStringField(
        srid=4326,
        null=True,
        blank=True,
        verbose_name="Use the map to estimate the distance.",
    )
    latitude = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Latitude",
    )
    longitude = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Longitude",
    )
    accuracy = models.FloatField(
        null=True,
        blank=True,
        verbose_name="GPS Accuracy",
    )
    irrigation_use = models.CharField(
        choices=(
            ("yes_en", "Yes"),
            ("no_en", "No"),
            ("yes_ro", "Da"),
            ("no_ro", "Nu"),
        ),
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Do you use water for irrigation?",
    )
    irrigation_interest = models.CharField(
        choices=(
            ("yes_en", "Yes"),
            ("no_en", "No"),
            ("yes_ro", "Da"),
            ("no_ro", "Nu"),
        ),
        max_length=6,
        null=True,
        blank=True,
        verbose_name="If not, do you have interest?",
    )
    irrigation_quantity = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Quantity (in m³ per year)",
    )
    irrigation_quality = models.CharField(
        choices=(
            ("source_en", "From source"),
            ("underground_en", "Underground water"),
            ("source_ro", "Din sursă"),
            ("underground_ro", "Apă subterană"),
        ),
        max_length=14,
        null=True,
        blank=True,
        verbose_name="Water quality",
    )
    electrical_consumption = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Average electrical consumption (in kWh per year)",
    )
    distance = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Distance: producer → storage → sale point (km)",
    )
    production = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Production (in kg/ha per year)",
    )
    surface = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Surface (in ha)",
    )
    use = models.CharField(
        choices=(
            ("homefood_en", "Homefood"),
            ("other_en", "Other"),
            ("homefood_ro", "Uz casnic"),
            ("other_ro", "Alte utilizări alimentare"),
        ),
        max_length=11,
        null=True,
        blank=True,
        verbose_name="Uses",
    )
    fertilizer = models.CharField(
        choices=(
            ("natural_en", "Natural"),
            ("artificial_en", "Artificial"),
            ("natural_ro", "Naturale"),
            ("artificial_ro", "Artificiale"),
        ),
        max_length=13,
        null=True,
        blank=True,
        verbose_name="Use of fertilizer",
    )
    storagepoint = models.ForeignKey(
        "storagepoint.Storagepoint",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Storage point",
    )
    salepoint = models.ForeignKey(
        "salepoint.Salepoint",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Sale point",
    )

    wq_label_template = "{{name}}"

    def __str__(self):
        return pystache.render(self.wq_label_template, self)

    class Meta:
        verbose_name = "producer"
        verbose_name_plural = "producers"

class Photo(models.Model):
    producer = models.ForeignKey(
        Producer,
        on_delete=models.CASCADE,
        related_name="photos",
    )
    picture = models.ImageField(
        upload_to="producers",
        null=True,
        blank=True,
        verbose_name="Picture of products/location",
    )

    def __label__(self):
        return self.picture and self.picture.name

    class Meta:
        verbose_name = "photo"
        verbose_name_plural = "photos"
