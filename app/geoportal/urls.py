from django.urls import path
from .views import (
    LakeOrPondAPIView, 
    LakeOrPond1827APIView, 
    LakeOrPond1884APIView,
    LakeOrPond1965APIView, 
    LakeOrPond2009APIView, 
    BuildingAPIView, 
    Building1827APIView, 
    Building1884APIView, 
    Building1965APIView,
    Building2009APIView, 
    CompactSettlementAPIView,
    CompactSettlement1827APIView,
    CompactSettlement1884APIView,
    CompactSettlement1965APIView,
    CompactSettlement2009APIView,
    ForestAPIView,
    Forest1827APIView,
    Forest1884APIView,
    Forest1965APIView,
    Forest2009APIView,
    MeadowOrPastureAPIView,
    MeadowOrPasture1827APIView,
    MeadowOrPasture1884APIView,
    MeadowOrPasture1965APIView,
    MeadowOrPasture2009APIView,
    OtherTypeAPIView,
    OtherType1827APIView,
    OtherType1884APIView,
    OtherType2009APIView,
    MultiOtherType1827APIView,
    MultiOtherType1884APIView,
    MultiOtherType1965APIView,
    MultiOtherType2009APIView,
    RiverAPIView,
    River1827APIView,
    River1884APIView,
    River1965APIView,
    River2009APIView,
    RoadAPIView,
    Road1827APIView,
    Road1884APIView,
    Road1965APIView,
    Road2009APIView,
    HighwayFieldAPIView
)


urlpatterns = [
    path('api/lakes-ponds/', LakeOrPondAPIView.as_view(), name='lake_or_pond_api'),
    path('api/lakes-ponds/1827/', LakeOrPond1827APIView.as_view(), name='lake_or_pond_1827_api'),
    path('api/lakes-ponds/1884/', LakeOrPond1884APIView.as_view(), name='lake_or_pond_1884_api'),
    path('api/lakes-ponds/1965/', LakeOrPond1965APIView.as_view(), name='lake_or_pond_1965_api'),
    path('api/lakes-ponds/2009/', LakeOrPond2009APIView.as_view(), name='lake_or_pond_2009_api'),
    path('api/buildings/', BuildingAPIView.as_view(), name='building_api'),
    path('api/buildings/1827/', Building1827APIView.as_view(), name='building_1827_api'),
    path('api/buildings/1884/', Building1884APIView.as_view(), name='building_1884_api'),
    path('api/buildings/1965/', Building1965APIView.as_view(), name='building_1965_api'),
    path('api/buildings/2009/', Building2009APIView.as_view(), name='building_2009_api'),
    path('api/settlements/', CompactSettlementAPIView.as_view(), name='compact_settlements_api'),
    path('api/settlements/1827/', CompactSettlement1827APIView.as_view(), name='compact_settlements_1827_api'),
    path('api/settlements/1884/', CompactSettlement1884APIView.as_view(), name='compact_settlements_1884_api'),
    path('api/settlements/1965/', CompactSettlement1965APIView.as_view(), name='compact_settlements_1965_api'),
    path('api/settlements/2009/', CompactSettlement2009APIView.as_view(), name='compact_settlements_2009_api'),
    path('api/forests/', ForestAPIView.as_view(), name='forest_api'),
    path('api/forests/1827/', Forest1827APIView.as_view(), name='forest_1827_api'),
    path('api/forests/1884/', Forest1884APIView.as_view(), name='forest_1884_api'),
    path('api/forests/1965/', Forest1965APIView.as_view(), name='forest_1965_api'),
    path('api/forests/2009/', Forest2009APIView.as_view(), name='forest_2009_api'),
    path('api/meadows-pastures/', MeadowOrPastureAPIView.as_view(), name='meadow_or_pasture_api'),
    path('api/meadows-pastures/1827/', MeadowOrPasture1827APIView.as_view(), name='meadow_or_pasture_1827_api'),
    path('api/meadows-pastures/1884/', MeadowOrPasture1884APIView.as_view(), name='meadow_or_pasture_1884_api'),
    path('api/meadows-pastures/1965/', MeadowOrPasture1965APIView.as_view(), name='meadow_or_pasture_1965_api'),    
    path('api/meadows-pastures/2009/', MeadowOrPasture2009APIView.as_view(), name='meadow_or_pasture_2009_api'),
    path('api/other-types/', OtherTypeAPIView.as_view(), name='other_type_api'),
    path('api/other-types/1827/', OtherType1827APIView.as_view(), name='other_type_1827_api'),
    path('api/other-types/1884/', OtherType1884APIView.as_view(), name='other_type_1884_api'),
    path('api/other-types/2009/', OtherType2009APIView.as_view(), name='other_type_2009_api'),
    path('api/multi-other-types/1827/', MultiOtherType1827APIView.as_view(), name='multi_other_type_1827_api'),
    path('api/multi-other-types/1884/', MultiOtherType1884APIView.as_view(), name='multi_other_type_1884_api'),
    path('api/multi-other-types/1965/', MultiOtherType1965APIView.as_view(), name='multi_other_type_1965_api'),
    path('api/multi-other-types/2009/', MultiOtherType2009APIView.as_view(), name='multi_other_type_2009_api'),
    path('api/rivers/', RiverAPIView.as_view(), name='river_api'),
    path('api/rivers/1827/', River1827APIView.as_view(), name='river_1827_api'),
    path('api/rivers/1884/', River1884APIView.as_view(), name='river_1884_api'),
    path('api/rivers/1965/', River1965APIView.as_view(), name='river_1965_api'),
    path('api/rivers/2009/', River2009APIView.as_view(), name='river_2009_api'),
    path('api/roads/', RoadAPIView.as_view(), name='road_api'),
    path('api/roads/1827/', Road1827APIView.as_view(), name='road_1827_api'),
    path('api/roads/1884/', Road1884APIView.as_view(), name='road_1884_api'),
    path('api/roads/1965/', Road1965APIView.as_view(), name='road_1965_api'),
    path('api/roads/2009/', Road2009APIView.as_view(), name='road_2009_api'),
    path('api/highway/', HighwayFieldAPIView.as_view(), name='highway_api'),
]
