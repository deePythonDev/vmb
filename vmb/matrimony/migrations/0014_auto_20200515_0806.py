# Generated by Django 2.2.7 on 2020-05-15 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony', '0013_merge_20200515_0715'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'caste',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Degree')),
            ],
            options={
                'db_table': 'education',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='EducationCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=75, unique=True)),
            ],
            options={
                'db_table': 'education_category',
            },
        ),
        migrations.CreateModel(
            name='OccupationCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=75, unique=True)),
            ],
            options={
                'db_table': 'occupation_category',
            },
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'religion',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Subcaste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20)),
                ('caste', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matrimony.Caste')),
            ],
            options={
                'db_table': 'subcaste',
                'ordering': ['name'],
            },
        ),
        migrations.RemoveField(
            model_name='matrimonyprofile',
            name='qualification',
        ),
        migrations.AddField(
            model_name='matrimonyprofile',
            name='body_type',
            field=models.CharField(blank=True, choices=[('SLM', 'Slim'), ('AVG', 'Average'), ('ATH', 'Athelete'), ('HEA', 'Heavy')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='matrimonyprofile',
            name='mother_tongue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='matrimony.Language'),
        ),
        migrations.AlterField(
            model_name='matrimonyprofile',
            name='occupation',
            field=models.ForeignKey(help_text='Doctor, Engineer, Entrepreneur etc.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='matrimony.Occupation'),
        ),
        migrations.AlterField(
            model_name='matrimonyprofile',
            name='religion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='matrimony.Religion'),
        ),
        migrations.DeleteModel(
            name='Qualification',
        ),
        migrations.AddField(
            model_name='education',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='matrimony.EducationCategory'),
        ),
        migrations.AddField(
            model_name='matrimonyprofile',
            name='caste',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='matrimony.Caste'),
        ),
        migrations.AddField(
            model_name='matrimonyprofile',
            name='education',
            field=models.ForeignKey(help_text='HS, Graduate etc.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='matrimony.Education'),
        ),
        migrations.AddField(
            model_name='matrimonyprofile',
            name='subcaste',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='matrimony.Subcaste'),
        ),
        migrations.AddField(
            model_name='occupation',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='matrimony.OccupationCategory'),
        ),
    ]