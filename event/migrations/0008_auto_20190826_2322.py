# Generated by Django 2.2 on 2019-08-27 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_auto_20190826_2248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='is_published',
            new_name='is_publish',
        ),
        migrations.AddField(
            model_name='event',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
