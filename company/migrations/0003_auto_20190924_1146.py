# Generated by Django 2.2 on 2019-09-24 18:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20190429_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
