# Generated by Django 2.2 on 2019-05-10 20:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('jobapps', '0026_auto_20190501_0453'),
    ]

    operations = [
        migrations.AddField(
            model_name='googlemail',
            name='app_source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='googlemail_source', to='jobapps.Source'),
        ),
    ]
