from django.contrib.gis.db import models


class Energyusage(models.Model):
    energy_type = models.CharField(
        choices=(
            ("national_en", "National system"),
            ("renewable_en", "Renewable"),
            ("both_en", "Both"),
            ("national_ro", "Sistem Național"),
            ("renewable_ro", "Regenerabilă"),
            ("both_ro", "Amândouă"),
        ),
        max_length=9,
        null=True,
        blank=True,
        verbose_name="What type of energy do you use?",
    )
    more_renewable = models.CharField(
        choices=(
            ("yes_en", "Yes"),
            ("no_en", "No"),
            ("yes_ro", "Da"),
            ("no_ro", "Nu"),
        ),
        max_length=3,
        null=True,
        blank=True,
        verbose_name="Would you like to use more renewable energy?",
    )
    renewable_type = models.CharField(
        choices=(
            ("solar_en", "Solar"),
            ("wind_en", "Wind"),
            ("water_en", "Water"),
            ("geothermal_en", "Geothermal"),
            ("bio_en", "Bio"),
            ("other_en", "Other"),
            ("solar_ro", "Solar"),
            ("wind_ro", "Vânt"),
            ("water_ro", "Apă"),
            ("geothermal_ro", "Geotermală"),
            ("bio_ro", "Bio"),
            ("other_ro", "Alte"),
        ),
        max_length=10,
        null=True,
        blank=True,
        verbose_name="What type of renewable energy do you use?",
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

    class Meta:
        verbose_name = "energyusage"
        verbose_name_plural = "energyusages"
