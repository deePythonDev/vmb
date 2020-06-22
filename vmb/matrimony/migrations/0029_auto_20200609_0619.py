# Generated by Django 2.2.7 on 2020-06-09 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony', '0028_auto_20200608_0542'),
    ]

    operations = [
        migrations.AddField(
            model_name='expectation',
            name='chant_16_round',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=1, null=True, verbose_name='Does the spouse have to chant 16 rounds?'),
        ),
        migrations.AddField(
            model_name='expectation',
            name='color_of_eyes',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='expectation',
            name='four_reg_principles',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=1, null=True, verbose_name='Does the spouse have to follow four regulative principles?'),
        ),
        migrations.AddField(
            model_name='expectation',
            name='hair_color',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]