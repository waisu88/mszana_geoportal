import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')  # Wskaż ścieżkę do pliku settings.py
django.setup()

from geoportal.models import LakeOrPond, River, Road, Building, MeadowOrPasture, Forest, MultiOtherType, OtherType, CompactSettlement
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon, Polygon
import json

def handle(*args, **kwargs):
    years = ["1827", "1884", "2009"]
    for year in years:

        with open(f'{year}_pozostale_converted.geojson', 'r') as file:
            data = json.load(file)
            print(data)
   
            # for feature in data['features']:
            #     geometry = GEOSGeometry(json.dumps(feature['geometry']))
            #     print(feature)
            #     if geometry.geom_type == 'MultiPolygon':
            #         # Wybierz pierwszy Polygon z MultiPolygon
            #         geometry = geometry[0]
                
            #     if geometry.geom_type == 'Polygon':
            #         # Zapisz geometrię do bazy danych
            #         CompactSettlement.objects.create(year=year, geometry=geometry)
            for feature in data['features']:
                geometry = GEOSGeometry(json.dumps(feature['geometry']))

                # Obsługa MultiPolygon -> Polygon
                if geometry.geom_type == 'Polygon':
                    geometry = MultiPolygon(geometry)
                MultiOtherType.objects.create(year=year, geometry=geometry)
                
                # geometry = GEOSGeometry(json.dumps(feature['geometry']))
                # OtherType.objects.create(year=year, geometry=geometry)
                # else:
                #     print(f"Pomijam nieobsługiwany typ geometrii: {geometry.geom_type}")
handle()