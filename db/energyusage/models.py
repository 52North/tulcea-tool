from django.contrib.gis.db import models


class Energyusage(models.Model):
    energy_type = models.CharField(
        choices=(
            ("national", "National system"),
            ("renewable", "Renewable"),
            ("both", "Both"),
        ),
        max_length=9,
        null=True,
        blank=True,
        verbose_name="What type of energy do you use?",
    )
    more_renewable = models.CharField(
        choices=(
            ("yes", "Yes"),
            ("no", "No"),
        ),
        max_length=3,
        null=True,
        blank=True,
        verbose_name="Would you like to use more renewable energy?",
    )
    renewable_type = models.CharField(
        choices=(
            ("solar", "Solar"),
            ("wind", "Wind"),
            ("water", "Water"),
            ("geothermal", "Geothermal"),
            ("bio", "Bio"),
            ("other", "Other"),
        ),
        max_length=10,
        null=True,
        blank=True,
        verbose_name="What type of renewable energy do you use?",
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
