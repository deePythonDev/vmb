# Generated by Django 2.2.7 on 2020-05-10 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0011_auto_20190223_2138'),
        ('matrimony', '0010_emailmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('primary', models.BooleanField(blank=True, default=False)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='photologue.Photo')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matrimony.MatrimonyProfile')),
            ],
            options={
                'db_table': 'matrimony_images',
            },
        ),
        migrations.AddField(
            model_name='matrimonyprofile',
            name='images',
            field=models.ManyToManyField(blank=True, through='matrimony.Image', to='photologue.Photo'),
        ),
    ]
