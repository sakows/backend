# Generated by Django 2.2 on 2019-08-08 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_remove_event_view_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='short_description',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
