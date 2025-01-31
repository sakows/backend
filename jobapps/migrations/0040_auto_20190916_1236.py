# Generated by Django 2.2 on 2019-09-16 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapps', '0039_auto_20190821_0650'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applicationstatus',
            options={'ordering': ['pos'], 'verbose_name': 'status', 'verbose_name_plural': 'statuses'},
        ),
        migrations.AddField(
            model_name='applicationstatus',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='applicationstatus',
            name='pos',
            field=models.SmallIntegerField(default='0', verbose_name='position'),
        ),
    ]
