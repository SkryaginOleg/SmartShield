# Generated by Django 5.1.3 on 2024-12-25 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incidentreport',
            name='camera',
        ),
        migrations.RemoveField(
            model_name='incidentreport',
            name='sensor',
        ),
        migrations.AddField(
            model_name='incidentreport',
            name='IPN',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incidentreport',
            name='location',
            field=models.CharField(default='location1', max_length=100),
            preserve_default=False,
        ),
    ]
