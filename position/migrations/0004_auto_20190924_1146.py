# Generated by Django 2.2 on 2019-09-24 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0003_auto_20190510_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobposition',
            name='job_title',
            field=models.CharField(default=111, max_length=200),
            preserve_default=False,
        ),
    ]
