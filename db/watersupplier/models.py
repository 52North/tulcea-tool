from django.contrib.gis.db import models
import pystache


class Watersupplier(models.Model):
    name = models.TextField(
        null=True,
        blank=True,
        verbose_name="Name",
    )
    type = models.TextField(
        null=True,
        blank=True,
        verbose_name="Type of supplier",
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
    bogza = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Bogza (in m³)",
    )
    mila = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Mila (in m³)",
    )
    irrigation_supply = models.CharField(
        choices=(
            ("source_en", "From source"),
            ("underground_en", "Underground water"),
            ("source_ro", "Din sursă"),
            ("underground_ro", "Apă subterană"),
        ),
        max_length=14,
        null=True,
        blank=True,
        verbose_name="Irrigation supply",
    )

    wq_label_template = "{{name}}"

    def __str__(self):
        return pystache.render(self.wq_label_template, self)

    class Meta:
        verbose_name = "watersupplier"
        verbose_name_plural = "watersuppliers"
