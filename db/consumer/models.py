from django.db import models


class Consumer(models.Model):
    gender = models.TextField(
        null=True,
        blank=True,
        verbose_name="Gender",
    )
    age = models.CharField(
        choices=(
            ("12_20", "12-20"),
            ("20_35", "20-35"),
            ("35_55", "35-55"),
            ("older_55", "55+"),
        ),
        max_length=8,
        null=True,
        blank=True,
        verbose_name="Age",
    )
    income = models.CharField(
        choices=(
            ("less_1500", "&lt; 1500 / family member"),
            ("more_1500", "&gt; 1500 / family member"),
            ("na", "NA"),
        ),
        max_length=9,
        null=True,
        blank=True,
        verbose_name="Income (Euro)",
    )
    big_chain_store = models.CharField(
        choices=(
            ("1", "1"),
            ("3", "ca. 3"),
            ("more", "More"),
        ),
        max_length=4,
        null=True,
        blank=True,
        verbose_name="Big store chains",
    )
    local_chain_store = models.CharField(
        choices=(
            ("1", "1"),
            ("3", "ca. 3"),
            ("more", "More"),
        ),
        max_length=4,
        null=True,
        blank=True,
        verbose_name="Local chain stores",
    )
    small_shop = models.CharField(
        choices=(
            ("1", "1"),
            ("3", "ca. 3"),
            ("more", "More"),
        ),
        max_length=4,
        null=True,
        blank=True,
        verbose_name="Small shops",
    )
    market = models.CharField(
        choices=(
            ("1", "1"),
            ("3", "ca. 3"),
            ("more", "More"),
        ),
        max_length=4,
        null=True,
        blank=True,
        verbose_name="Market",
    )
    transport = models.CharField(
        choices=(
            ("car", "Personal car"),
            ("public", "Public transport"),
            ("bike", "By bike"),
            ("foot", "By foot"),
        ),
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Main transport",
    )
    bio = models.CharField(
        choices=(
            ("frequently", "Frequently"),
            ("sometimes", "Sometimes"),
            ("no_use", "No use"),
        ),
        max_length=10,
        null=True,
        blank=True,
        verbose_name="Bio products use",
    )
    local = models.CharField(
        choices=(
            ("frequently", "Frequently"),
            ("sometimes", "Sometimes"),
            ("no_use", "No use"),
        ),
        max_length=10,
        null=True,
        blank=True,
        verbose_name="Local/national products use",
    )
    tap_water_quantity = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Quantity of consumed tap water (in m³)",
    )
    bottled_water_quantity = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Quantity of consumed bottled water (in m³)",
    )
    waste_water = models.CharField(
        choices=(
            ("sewage", "Sewage system"),
            ("septic", "Septic tanks"),
            ("no_treatment", "No treatment at all"),
        ),
        max_length=12,
        null=True,
        blank=True,
        verbose_name="Waste water",
    )
    priorization = models.CharField(
        choices=(
            ("price", "Price"),
            ("ecological_impact", "Ecological impact"),
            ("aquisition_time", "Time for aquisition"),
            ("health_impact", "Health impact"),
        ),
        max_length=17,
        null=True,
        blank=True,
        verbose_name="Priorization in food choice",
    )

    class Meta:
        verbose_name = "consumer"
        verbose_name_plural = "consumers"
