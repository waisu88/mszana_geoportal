# Generated by Django 5.1.3 on 2025-02-01 19:30

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoportal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HighwayField',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('geometry', django.contrib.gis.db.models.fields.PolygonField(srid=4326, verbose_name='Geometry')),
                ('year', models.CharField(blank=True, max_length=4, null=True)),
            ],
        ),
    ]
