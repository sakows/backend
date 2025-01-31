# Generated by Django 2.2 on 2019-04-28 01:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='faq title')),
                ('description', models.CharField(max_length=250, verbose_name='faq description')),
                ('is_published', models.BooleanField(default=True, verbose_name='is published')),
                ('position', models.SmallIntegerField(default=0, verbose_name='position')),
            ],
            options={
                'verbose_name': 'faq',
                'verbose_name_plural': 'faqs',
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=250, verbose_name='value')),
                ('position', models.SmallIntegerField(default=0, verbose_name='position')),
                ('faq',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='faq.Faq')),
            ],
            options={
                'verbose_name': 'items',
                'verbose_name_plural': 'items',
                'ordering': ['position'],
            },
        ),
    ]
