from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import (
LakeOrPond, 
River, 
Road, 
Building, 
CompactSettlement, 
OtherType, 
MultiOtherType,
MeadowOrPasture, 
Forest,
HighwayField
)


class LakeOrPondSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = LakeOrPond
        fields = ["id", "geometry", "year"]
        geo_field = "geometry"

    
class RiverSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = River
        fields = ["id", "geometry", "year"]
        geo_field = "geometry"


class RoadSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Road
        fields = ["id", "geometry", "year"]
        geo_field = "geometry"


class BuildingSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Building
        fields = ["id", "geometry", "year"]
        geo_field = "geometry"


class CompactSettlementSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = CompactSettlement
        fields = ["id", "geometry", "year"]
        geo_field = "geometry"


class OtherTypeSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = OtherType
        fields = ["id", "geometry", "year"]
        geo_field = "geometry"

class MultiOtherTypeSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MultiOtherType
        fields = ["id", "geometry", "year"]
        geo_field = "geometry"


class MeadowOrPastureSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MeadowOrPasture
        fields = ["id", "geometry", "year"]
        geo_field = "geometry"


class ForestSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Forest
        fields = ["id", "geometry", "year"]
        geo_field = "geometry"


class HigwayFieldSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = HighwayField
        fields = ["id", "geometry", "year"]
        geo_field = "geometry"