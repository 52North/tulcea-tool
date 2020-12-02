from django.contrib.gis.db import models
import pystache


class Storagepoint(models.Model):
    name = models.TextField(
        null=True,
        blank=True,
        verbose_name="Name",
    )
    type = models.TextField(
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

    wq_label_template = "{{name}}"

    def __str__(self):
        return pystache.render(self.wq_label_template, self)

    class Meta:
        verbose_name = "storagepoint"
        verbose_name_plural = "storagepoints"
