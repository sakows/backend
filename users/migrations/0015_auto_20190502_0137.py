# Generated by Django 2.2 on 2019-05-02 01:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0014_auto_20190502_0129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='activation_key',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='key_expires',
        ),
        migrations.AddField(
            model_name='user',
            name='activation_key',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='key_expires',
            field=models.DateTimeField(null=True),
        ),
    ]
