from django.contrib.gis import admin

from .models import (
LakeOrPond, River, Road, Building, CompactSettlement, OtherType, MeadowOrPasture, Forest
)
# admin.site.register(Category)

class CustomGeoAdmin(admin.GISModelAdmin):
    gis_widget_kwargs= {
        'attrs': {
            'default_zoom': 14,
            'default_lon': 18.546,
            'default_lat': 50.00,
        },
        
    }

    


@admin.register(LakeOrPond)
class LakeOrPondAdmin(CustomGeoAdmin):
    pass

@admin.register(River)
class RiverAdmin(CustomGeoAdmin):
    pass

@admin.register(Road)
class RoadAdmin(CustomGeoAdmin):
    pass

@admin.register(Building)
class BuildingAdmin(CustomGeoAdmin):
    pass

@admin.register(CompactSettlement)
class CompactSettlementAdmin(CustomGeoAdmin):
    pass

@admin.register(OtherType)
class OtherTypeAdmin(CustomGeoAdmin):
    pass

@admin.register(MeadowOrPasture)
class MeadowOrPastureAdmin(CustomGeoAdmin):
    pass

@admin.register(Forest)
class ForestAdmin(CustomGeoAdmin):
    pass
