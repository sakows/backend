# Generated by Django 2.2 on 2019-08-04 03:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0026_auto_20190804_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='grad_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
