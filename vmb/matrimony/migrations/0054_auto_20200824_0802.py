# Generated by Django 2.2.7 on 2020-08-24 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony', '0053_auto_20200824_0757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matrimonyprofile',
            old_name='father_occupation',
            new_name='father_status',
        ),
        migrations.RenameField(
            model_name='matrimonyprofile',
            old_name='mother_occupation',
            new_name='mother_status',
        ),
    ]
