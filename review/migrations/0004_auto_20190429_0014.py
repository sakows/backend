# Generated by Django 2.2 on 2019-04-29 00:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('review', '0003_auto_20190426_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='overall_interview_experience',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(5),
                                                                         django.core.validators.MinValueValidator(0)]),
        ),
    ]
