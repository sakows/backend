# Generated by Django 2.2 on 2019-04-29 19:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('review', '0005_auto_20190429_0046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-created_date']},
        ),
    ]
