from django.db import models
import pystache
from datetime import datetime


class Feedback(models.Model):
    rank_info_consumer = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Information about consumers and consumers profile",
    )
    rank_info_storage = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Information on storage points",
    )
    rank_info_producer_seller = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Information on local food producers/sellers ",
    )
    rank_info_production_service = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Information on production service ",
    )
    rank_info_energy_usage = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Evaluations of energy usage",
    )
    rank_info_water_supplier = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Information about water supplier",
    )
    rank_feature_see_producer_seller = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Access to information on local food producers/sellers",
    )
    rank_feature_see_water_supplier = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Access to information on water supplier",
    )
    rank_feature_add_producer_seller = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Possibility to add a local food producer/seller on the map",
    )
    rank_feature_see_energy_usage = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Access to information on energy usage",
    )
    rank_feature_add_by_others = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Possibility to see the information added by other users",
    )
    rank_feature_add_comment = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Leave a comment (open question)",
    )
    usability = models.CharField(
        choices=(
            ("strong_agree_en", "I strongly agree"),
            ("rather_agree_en", "I&#x27;d rather agree"),
            ("undecided_en", "Neither disagree nor agree"),
            ("rather_disagree_en", "I&#x27;d rather disagree"),
            ("strong_disagree_en", "I strongly disagree"),
            ("strong_agree_ro", "Total de acord"),
            ("rather_agree_ro", "De acord"),
            ("undecided_ro", "Indecis"),
            ("rather_disagree_ro", "Nu sunt de acord"),
            ("strong_disagree_ro", "Dezacord total"),
        ),
        max_length=18,
        null=True,
        blank=True,
        verbose_name="The application is easy to use",
    )
    attractiveness = models.CharField(
        choices=(
            ("strong_agree_en", "I strongly agree"),
            ("rather_agree_en", "I&#x27;d rather agree"),
            ("undecided_en", "Neither disagree nor agree"),
            ("rather_disagree_en", "I&#x27;d rather disagree"),
            ("strong_disagree_en", "I strongly disagree"),
            ("strong_agree_ro", "Total de acord"),
            ("rather_agree_ro", "De acord"),
            ("undecided_ro", "Indecis"),
            ("rather_disagree_ro", "Nu sunt de acord"),
            ("strong_disagree_ro", "Dezacord total"),
        ),
        max_length=18,
        null=True,
        blank=True,
        verbose_name="The application is visually (graphically) attractive",
    )
    maps = models.CharField(
        choices=(
            ("strong_agree_en", "I strongly agree"),
            ("rather_agree_en", "I&#x27;d rather agree"),
            ("undecided_en", "Neither disagree nor agree"),
            ("rather_disagree_en", "I&#x27;d rather disagree"),
            ("strong_disagree_en", "I strongly disagree"),
            ("strong_agree_ro", "Total de acord"),
            ("rather_agree_ro", "De acord"),
            ("undecided_ro", "Indecis"),
            ("rather_disagree_ro", "Nu sunt de acord"),
            ("strong_disagree_ro", "Dezacord total"),
        ),
        max_length=18,
        null=True,
        blank=True,
        verbose_name="Maps help to use the application",
    )
    clarity = models.CharField(
        choices=(
            ("strong_agree_en", "I strongly agree"),
            ("rather_agree_en", "I&#x27;d rather agree"),
            ("undecided_en", "Neither disagree nor agree"),
            ("rather_disagree_en", "I&#x27;d rather disagree"),
            ("strong_disagree_en", "I strongly disagree"),
            ("strong_agree_ro", "Total de acord"),
            ("rather_agree_ro", "De acord"),
            ("undecided_ro", "Indecis"),
            ("rather_disagree_ro", "Nu sunt de acord"),
            ("strong_disagree_ro", "Dezacord total"),
        ),
        max_length=18,
        null=True,
        blank=True,
        verbose_name="Instruction on how to use the application is easy to understand",
    )
    usefulness = models.CharField(
        choices=(
            ("definitely_yes_en", "Definitely yes"),
            ("rather_yes_en", "Rather yes"),
            ("no_opinion_en", "I have no opinion"),
            ("rather_not_en", "Rather not"),
            ("definitely_not_en", "Definitely not"),
            ("definitely_yes_ro", "Total de acord"),
            ("rather_yes_ro", "De acord"),
            ("no_opinion_ro", "Indecis"),
            ("rather_not_ro", "Nu sunt de acord"),
            ("definitely_not_ro", "Dezacord total"),
        ),
        max_length=17,
        null=True,
        blank=True,
        verbose_name="Do you think that the data collected through the application can be useful for a better representation of local producers and small gardeners?",
    )
    comment = models.TextField(
        null=True,
        blank=True,
        verbose_name="What other functions should the application have?",
    )

    wq_label_template = "Feedback from/de la " + datetime.today().strftime('%Y-%m-%d')

    def __str__(self):
        return pystache.render(self.wq_label_template, self)

    class Meta:
        verbose_name = "feedback"
        verbose_name_plural = "feedbacks"
