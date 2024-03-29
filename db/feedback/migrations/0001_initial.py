# Generated by Django 2.2.3 on 2020-06-16 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usability', models.CharField(blank=True, choices=[('strong_agree', 'I strongly agree'), ('rather_agree', 'I&#x27;d rather agree'), ('undecided', 'Neither disagree nor agree'), ('rather_disagree', 'I&#x27;d rather disagree'), ('strong_disagree', 'I strongly disagree')], max_length=15, null=True, verbose_name='The application is useful')),
                ('attractiveness', models.CharField(blank=True, choices=[('strong_agree', 'I strongly agree'), ('rather_agree', 'I&#x27;d rather agree'), ('undecided', 'Neither disagree nor agree'), ('rather_disagree', 'I&#x27;d rather disagree'), ('strong_disagree', 'I strongly disagree')], max_length=15, null=True, verbose_name='The application is visually (graphically) attractive')),
                ('maps', models.CharField(blank=True, choices=[('strong_agree', 'I strongly agree'), ('rather_agree', 'I&#x27;d rather agree'), ('undecided', 'Neither disagree nor agree'), ('rather_disagree', 'I&#x27;d rather disagree'), ('strong_disagree', 'I strongly disagree')], max_length=15, null=True, verbose_name='Maps help to use the application')),
                ('clarity', models.CharField(blank=True, choices=[('strong_agree', 'I strongly agree'), ('rather_agree', 'I&#x27;d rather agree'), ('undecided', 'Neither disagree nor agree'), ('rather_disagree', 'I&#x27;d rather disagree'), ('strong_disagree', 'I strongly disagree')], max_length=15, null=True, verbose_name='Instruction on how to use the application is easy to understand')),
                ('main_attraction', models.TextField(blank=True, null=True, verbose_name='What was the main attraction?')),
                ('other_function', models.TextField(blank=True, null=True, verbose_name='What other functions should the application have?')),
            ],
            options={
                'verbose_name': 'feedback',
                'verbose_name_plural': 'feedbacks',
            },
        ),
    ]
