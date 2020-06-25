from django.contrib.gis.db import models


class Productionservice(models.Model):
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
    raw_material = models.TextField(
        null=True,
        blank=True,
        verbose_name="Source of raw material",
    )
    water_quantity = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Water quantity need (in m³ per month)",
    )
    energy_consumption = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Average energy consumption (in kWh per month)",
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
    distance = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Distance: production site → storage → shop",
    )
    covid_affected = models.CharField(
        choices=(
            ("yes", "Yes"),
            ("no", "No"),
        ),
        max_length=3,
        null=True,
        blank=True,
        verbose_name="Are the measures taken in the context of limiting COVID-19 infection affecting you?",
    )
    main_effect = models.CharField(
        choices=(
            ("scaderea_vanzarilor", "Scăderea vânzărilor"),
            ("scaderea_cifrei", "Scăderea cifrei de afaceri"),
            ("disponibilizari", "Disponibilizări"),
            ("intarzieri", "Întârzieri la plata furnizorilor"),
            ("dificultati", "Dificultăţi la încasare"),
            ("restrangerea", "Restrângerea activității"),
            ("suspendarea", "Suspendarea temporară a activităţii"),
            ("inchiderea", "Închiderea firmei"),
            ("reprofilare", "Reprofilare"),
        ),
        max_length=19,
        null=True,
        blank=True,
        verbose_name="The main effect is",
    )
    turnover_decrease = models.CharField(
        choices=(
            ("0_20", "0 – 20 %"),
            ("20_40", "20 – 40 %"),
            ("40_60", "40 – 60 %"),
            ("More_60", "&gt; 60 %"),
        ),
        max_length=7,
        null=True,
        blank=True,
        verbose_name="What is the percentage by which you estimate the decrease in turnover?",
    )

    class Meta:
        verbose_name = "productionservice"
        verbose_name_plural = "productionservices"
