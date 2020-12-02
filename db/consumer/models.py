from django.db import models


class Consumer(models.Model):
    gender = models.CharField(
        choices=(
            ("male_en", "Male"),
            ("female_en", "Female"),
            ("male_ro", "Masculin"),
            ("female_ro", "Feminin"),
        ),
        max_length=9,
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
            ("less_1500_en", "&lt; 1500 / family member"),
            ("more_1500_en", "&gt; 1500 / family member"),
            ("na_en", "No answer"),
            ("less_1500_ro", "Sub 1500/per membru de familie"),
            ("more_1500_ro", "Peste 1500/per membru de familie"),
            ("na_ro", "Nu doresc sa răspund"),
        ),
        max_length=12,
        null=True,
        blank=True,
        verbose_name="Income (Euro)",
    )
    big_chain_store = models.CharField(
        choices=(
            ("1_en", "1"),
            ("3_en", "ca. 3"),
            ("more_en", "More"),
            ("1_ro", "1"),
            ("3_ro", "cca 3"),
            ("more_ro", "Mai multe"),
        ),
        max_length=7,
        null=True,
        blank=True,
        verbose_name="Big store chains",
    )
    local_chain_store = models.CharField(
        choices=(
            ("1_en", "1"),
            ("3_en", "ca. 3"),
            ("more_en", "More"),
            ("1_ro", "1"),
            ("3_ro", "cca 3"),
            ("more_ro", "Mai multe"),
        ),
        max_length=7,
        null=True,
        blank=True,
        verbose_name="Local chain stores",
    )
    small_shop = models.CharField(
        choices=(
            ("1_en", "1"),
            ("3_en", "ca. 3"),
            ("more_en", "More"),
            ("1_ro", "1"),
            ("3_ro", "cca 3"),
            ("more_ro", "Mai multe"),
        ),
        max_length=7,
        null=True,
        blank=True,
        verbose_name="Small shops",
    )
    market = models.CharField(
        choices=(
            ("1_en", "1"),
            ("3_en", "ca. 3"),
            ("more_en", "More"),
            ("1_ro", "1"),
            ("3_ro", "cca 3"),
            ("more_ro", "Mai multe"),
        ),
        max_length=7,
        null=True,
        blank=True,
        verbose_name="Market",
    )
    transport = models.CharField(
        choices=(
            ("car_en", "Personal car"),
            ("public_en", "Public transport"),
            ("bike_en", "By bike"),
            ("foot_en", "By foot"),
            ("car_ro", "Auto personal"),
            ("public_ro", "Transport public"),
            ("bike_ro", "Bicicletă"),
            ("foot_ro", "Pedestru"),
        ),
        max_length=9,
        null=True,
        blank=True,
        verbose_name="Main transport",
    )
    bio = models.CharField(
        choices=(
            ("frequently_en", "Frequently"),
            ("sometimes_en", "Sometimes"),
            ("no_use_en", "No use"),
            ("frequently_ro", "Frecvent"),
            ("sometimes_ro", "Uneori"),
            ("no_use_ro", "Niciodata"),
        ),
        max_length=13,
        null=True,
        blank=True,
        verbose_name="Bio products use",
    )
    local = models.CharField(
        choices=(
            ("frequently_en", "Frequently"),
            ("sometimes_en", "Sometimes"),
            ("no_use_en", "No use"),
            ("frequently_ro", "Frecvent"),
            ("sometimes_ro", "Uneori"),
            ("no_use_ro", "Niciodata"),
        ),
        max_length=13,
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
            ("sewage_en", "Sewage system"),
            ("septic_en", "Septic tanks"),
            ("no_treatment_en", "No treatment at all"),
            ("sewage_ro", "Sistem centralizat de canalizare"),
            ("septic_ro", "Fosă septică"),
            ("no_treatment_ro", "Nici unul"),
        ),
        max_length=15,
        null=True,
        blank=True,
        verbose_name="Waste water",
    )
    priorization = models.CharField(
        choices=(
            ("price_en", "Price"),
            ("ecological_impact_en", "Ecological impact"),
            ("aquisition_time_en", "Time for aquisition"),
            ("health_impact_en", "Health impact"),
            ("price_ro", "Prețul"),
            ("ecological_impact_ro", "Impactul ecologic"),
            ("aquisition_time_ro", "Timpul consumat pentru cumpărături (distanța până la magazin)"),
            ("health_impact_ro", "Impactul asupra sănătății"),
        ),
        max_length=20,
        null=True,
        blank=True,
        verbose_name="Priorization in food choice",
    )

    class Meta:
        verbose_name = "consumer"
        verbose_name_plural = "consumers"
