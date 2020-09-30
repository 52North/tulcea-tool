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
            ("certificate", "Certificate of producer"),
            ("small_company", "Small company"),
            ("small_gardening", "Small gardening"),
        ),
        max_length=15,
        null=True,
        blank=True,
        verbose_name="Type",
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
            ("gps", "Use GPS"),
            ("interactive", "Point on Map"),
            ("manual", "Enter Manually"),
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
            ("yes", "Yes"),
            ("no", "No"),
        ),
        max_length=3,
        null=True,
        blank=True,
        verbose_name="Do you use water for irrigation?",
    )
    irrigation_interest = models.CharField(
        choices=(
            ("yes", "Yes"),
            ("no", "No"),
        ),
        max_length=3,
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
            ("source", "From source"),
            ("underground", "Underground water"),
        ),
        max_length=11,
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
            ("homefood", "Homefood"),
            ("other", "Other"),
        ),
        max_length=8,
        null=True,
        blank=True,
        verbose_name="Uses",
    )
    fertilizer = models.CharField(
        choices=(
            ("natural", "Natural"),
            ("artificial", "Artificial"),
        ),
        max_length=10,
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
