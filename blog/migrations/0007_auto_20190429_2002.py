# Generated by Django 2.2 on 2019-04-29 20:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0006_auto_20190429_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author_image',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
