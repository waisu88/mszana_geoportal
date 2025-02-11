import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')  # Wskaż ścieżkę do pliku settings.py
django.setup()

from geoportal.models import LakeOrPond, River, Road, Building, MeadowOrPasture, Forest, MultiOtherType, OtherType, CompactSettlement, HighwayField
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon, Polygon
import json

def handle(*args, **kwargs):
    years = ["1827", "1884", "1965", "2009"]
    layers = ["liczba_domow", "jeziora_i_stawy", "laki_i_pastwiska", "lasy", "pozostale", "rzeki", "drogi", "zwarta_zabudowa", "autostrada"]
    for year in years:
        for layer in layers:
            try:
                with open(f'static/geojson/{year}_{layer}_converted.geojson', 'r') as file:
                    data = json.load(file)
                    for feature in data['features']:
                        geometry = GEOSGeometry(json.dumps(feature['geometry']))
                        if geometry.geom_type == 'Point':
                            Building.objects.create(year=year, geometry=geometry)
                        elif geometry.geom_type == 'LineString':
                            if layer == "rzeki":
                                River.objects.create(year=year, geometry=geometry)
                            elif layer == "drogi":
                                Road.objects.create(year=year, geometry=geometry)
                        else:
                            if layer == "jeziora_i_stawy":
                                if geometry.geom_type == 'Polygon':
                                    geometry = MultiPolygon(geometry)
                                LakeOrPond.objects.create(year=year, geometry=geometry)
                            elif layer == "laki_i_pastwiska":
                                #  Obsługa MultiPolygon -> Polygon
                                if geometry.geom_type == 'Polygon':
                                    geometry = MultiPolygon(geometry)
                                MeadowOrPasture.objects.create(year=year, geometry=geometry)
                            elif layer == "lasy":
                                Forest.objects.create(year=year, geometry=geometry)
                            elif layer == "zwarta_zabudowa":
                                if geometry.geom_type == 'Polygon':
                                    geometry = MultiPolygon(geometry)
                                CompactSettlement.objects.create(year=year, geometry=geometry)
                            elif layer == "autostada":
                                HighwayField.objects.create(year=year, geometry=geometry)
                            elif layer == "pozostale":
                                #  Obsługa MultiPolygon -> Polygon
                                if geometry.geom_type == 'Polygon':
                                    geometry = MultiPolygon(geometry)
                                MultiOtherType.objects.create(year=year, geometry=geometry)
                    print(f"wczytano-{layer}-{year}")   
            except FileNotFoundError:
                print(f"brak pliku-{layer}-{year}")
                #     if geometry.geom_type == 'MultiPolygon':
                #         # Wybierz pierwszy Polygon z MultiPolygon
                #         geometry = geometry[0]
                    
                
                    # else:
                    #     print(f"Pomijam nieobsługiwany typ geometrii: {geometry.geom_type}")
handle()