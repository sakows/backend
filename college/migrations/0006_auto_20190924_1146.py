# Generated by Django 2.2 on 2019-09-24 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0005_delete_major'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
