# Generated by Django 2.2 on 2019-04-26 02:10

from django.db import migrations


class Migration(migrations.Migration):

    def check_default_status(apps, schema_editor):
        ApplicationStatus = apps.get_model('jobapps', 'ApplicationStatus')
        if ApplicationStatus.objects.filter(default=True).count() == 0:
            if ApplicationStatus.objects.filter(value__iexact='Applied').count == 0:
                status = ApplicationStatus(value='Applied', default=True)
                status.save()
            else:
                status = ApplicationStatus.objects.filter(value='Applied')
                if status.count() == 0:
                    status = ApplicationStatus(value="Applied")
                else:
                    status = status[0]
                status.default = True
                status.save()

    dependencies = [
        ('jobapps', '0018_applicationstatus_default'),
    ]

    operations = [
        migrations.RunPython(check_default_status,
                             reverse_code=migrations.RunPython.noop)
    ]
