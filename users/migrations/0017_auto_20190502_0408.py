# Generated by Django 2.2 on 2019-05-02 04:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0016_auto_20190502_0138'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='change_password_key',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='change_password_key_expires',
            field=models.DateTimeField(null=True),
        ),
    ]
