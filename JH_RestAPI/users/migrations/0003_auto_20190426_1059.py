# Generated by Django 2.2 on 2019-04-26 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190426_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='itu_email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='itu email address'),
        ),
    ]
