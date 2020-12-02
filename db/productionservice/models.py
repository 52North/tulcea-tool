from django.contrib.gis.db import models
import pystache


class Productionservice(models.Model):
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
        verbose_name="Distance: production site → storage → sale point (km)",
    )
    covid_affected = models.CharField(
        choices=(
            ("yes_en", "Yes"),
            ("no_en", "No"),
            ("yes_ro", "Da"),
            ("no_ro", "Nu"),
        ),
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Are the measures taken in the context of limiting COVID-19 infection affecting you?",
    )
    main_effect = models.CharField(
        choices=(
            ("scaderea_vanzarilor_en", "Scăderea vânzărilor"),
            ("scaderea_cifrei_en", "Scăderea cifrei de afaceri"),
            ("disponibilizari_en", "Disponibilizări"),
            ("intarzieri_en", "Întârzieri la plata furnizorilor"),
            ("dificultati_en", "Dificultăţi la încasare"),
            ("restrangerea_en", "Restrângerea activității"),
            ("suspendarea_en", "Suspendarea temporară a activităţii"),
            ("inchiderea_en", "Închiderea firmei"),
            ("reprofilare_en", "Reprofilare"),
            ("scaderea_vanzarilor_ro", "Scăderea vânzărilor"),
            ("scaderea_cifrei_ro", "Scăderea cifrei de afaceri"),
            ("disponibilizari_ro", "Disponibilizări"),
            ("intarzieri_ro", "Întârzieri la plata furnizorilor"),
            ("dificultati_ro", "Dificultăţi la încasare"),
            ("restrangerea_ro", "Restrângerea activității"),
            ("suspendarea_ro", "Suspendarea temporară a activităţii"),
            ("inchiderea_ro", "Închiderea firmei"),
            ("reprofilare_ro", "Reprofilare"),
        ),
        max_length=22,
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

    wq_label_template = "{{name}}"

    def __str__(self):
        return pystache.render(self.wq_label_template, self)

    class Meta:
        verbose_name = "productionservice"
        verbose_name_plural = "productionservices"
