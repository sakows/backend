# Generated by Django 2.2 on 2019-04-26 21:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('jobapps', '0022_remove_jobapplication_source'),
    ]

    operations = [
        migrations.CreateModel(
            name='SourceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=20)),
            ],
        ),
    ]
