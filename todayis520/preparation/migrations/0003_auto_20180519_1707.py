# Generated by Django 2.0.5 on 2018-05-19 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preparation', '0002_auto_20180519_1703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='iwanttosay',
            old_name='animated',
            new_name='animate',
        ),
    ]