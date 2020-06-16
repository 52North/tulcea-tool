from django.db import models


class Feedback(models.Model):
    usability = models.CharField(
        choices=(
            ("strong_agree", "I strongly agree"),
            ("rather_agree", "I&#x27;d rather agree"),
            ("undecided", "Neither disagree nor agree"),
            ("rather_disagree", "I&#x27;d rather disagree"),
            ("strong_disagree", "I strongly disagree"),
        ),
        max_length=15,
        null=True,
        blank=True,
        verbose_name="The application is useful",
    )
    attractiveness = models.CharField(
        choices=(
            ("strong_agree", "I strongly agree"),
            ("rather_agree", "I&#x27;d rather agree"),
            ("undecided", "Neither disagree nor agree"),
            ("rather_disagree", "I&#x27;d rather disagree"),
            ("strong_disagree", "I strongly disagree"),
        ),
        max_length=15,
        null=True,
        blank=True,
        verbose_name="The application is visually (graphically) attractive",
    )
    maps = models.CharField(
        choices=(
            ("strong_agree", "I strongly agree"),
            ("rather_agree", "I&#x27;d rather agree"),
            ("undecided", "Neither disagree nor agree"),
            ("rather_disagree", "I&#x27;d rather disagree"),
            ("strong_disagree", "I strongly disagree"),
        ),
        max_length=15,
        null=True,
        blank=True,
        verbose_name="Maps help to use the application",
    )
    clarity = models.CharField(
        choices=(
            ("strong_agree", "I strongly agree"),
            ("rather_agree", "I&#x27;d rather agree"),
            ("undecided", "Neither disagree nor agree"),
            ("rather_disagree", "I&#x27;d rather disagree"),
            ("strong_disagree", "I strongly disagree"),
        ),
        max_length=15,
        null=True,
        blank=True,
        verbose_name="Instruction on how to use the application is easy to understand",
    )
    main_attraction = models.TextField(
        null=True,
        blank=True,
        verbose_name="What was the main attraction?",
    )
    other_function = models.TextField(
        null=True,
        blank=True,
        verbose_name="What other functions should the application have?",
    )

    class Meta:
        verbose_name = "feedback"
        verbose_name_plural = "feedbacks"
