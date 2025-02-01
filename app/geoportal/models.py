from django.contrib.gis.db import models

# Create your models here.

class LakeOrPond(models.Model):
    id  = models.AutoField(primary_key=True)
    geometry = models.PolygonField(srid=4326, verbose_name="Geometry")
    year = models.CharField(max_length=4, null=True, blank=True)

    def __str__(self):
        return self.year


class River(models.Model):
    id  = models.AutoField(primary_key=True)
    geometry = models.LineStringField(srid=4326, verbose_name="Geometry")
    year = models.CharField(max_length=4, null=True, blank=True)


class Road(models.Model):
    id  = models.AutoField(primary_key=True)
    geometry = models.LineStringField(srid=4326, verbose_name="Geometry")
    year = models.CharField(max_length=4, null=True, blank=True)


class CompactSettlement(models.Model):
    id  = models.AutoField(primary_key=True)
    geometry = models.PolygonField(srid=4326, verbose_name="Geometry")
    year = models.CharField(max_length=4, null=True, blank=True)

    def __str__(self):
        return self.year


class OtherType(models.Model):
    id  = models.AutoField(primary_key=True)
    geometry = models.PolygonField(srid=4326, verbose_name="Geometry")
    year = models.CharField(max_length=4, null=True, blank=True)


class MultiOtherType(models.Model):
    id  = models.AutoField(primary_key=True)
    geometry = models.MultiPolygonField(srid=4326, verbose_name="Geometry")
    year = models.CharField(max_length=4, null=True, blank=True)


class MeadowOrPasture(models.Model):
    id  = models.AutoField(primary_key=True)
    geometry = models.MultiPolygonField(srid=4326, verbose_name="Geometry")
    year = models.CharField(max_length=4, null=True, blank=True)


class Forest(models.Model):
    id  = models.AutoField(primary_key=True)
    geometry = models.PolygonField(srid=4326, verbose_name="Geometry")
    year = models.CharField(max_length=4, null=True, blank=True)


class Building(models.Model):
    id  = models.AutoField(primary_key=True)
    geometry = models.PointField(srid=4326, verbose_name="Geometry")
    year = models.CharField(max_length=4, null=True, blank=True)


class HighwayField(models.Model):
    id  = models.AutoField(primary_key=True)
    geometry = models.PolygonField(srid=4326, verbose_name="Geometry")
    year = models.CharField(max_length=4, null=True, blank=True)