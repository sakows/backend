# Generated by Django 2.2 on 2019-05-28 20:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('jobapps', '0029_auto_20190528_1955'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applicationstatus',
            options={'ordering': ['value']},
        ),
        migrations.AlterModelOptions(
            name='source',
            options={'ordering': ['value']},
        ),
    ]
