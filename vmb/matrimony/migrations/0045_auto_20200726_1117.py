# Generated by Django 2.2.7 on 2020-07-26 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony', '0044_auto_20200725_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matrimonyprofile',
            name='birth_tz',
        ),
        migrations.AlterField(
            model_name='matrimonyprofile',
            name='birth_city',
            field=models.CharField(blank=True, help_text='Enter birth village/town/city', max_length=200, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='matrimonyprofile',
            name='birth_country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='birthCountry', to='matrimony.Country', verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='matrimonyprofile',
            name='birth_state',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='State'),
        ),
    ]
