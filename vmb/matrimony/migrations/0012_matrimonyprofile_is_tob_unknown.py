# Generated by Django 2.2.7 on 2021-09-28 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony', '0011_auto_20210621_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='matrimonyprofile',
            name='is_tob_unknown',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='Is Birth Time unknown?'),
        ),
    ]