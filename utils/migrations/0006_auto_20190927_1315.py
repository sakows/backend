# Generated by Django 2.2 on 2019-09-27 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0005_feedbackanswer_feedbackquestion_feedbackquestionitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedbackanswer',
            old_name='poll',
            new_name='feedback_question',
        ),
    ]
