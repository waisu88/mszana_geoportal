from rest_framework import generics
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
from .serializers import (
    LakeOrPondSerializer, 
    BuildingSerializer, 
    CompactSettlementSerializer,  
    ForestSerializer, 
    MeadowOrPastureSerializer, 
    OtherTypeSerializer, 
    MultiOtherTypeSerializer,
    RiverSerializer, 
    RoadSerializer,
    HigwayFieldSerializer
)

# Widoki dla jezior i stawów
class LakeOrPondAPIView(generics.ListAPIView):
    queryset = LakeOrPond.objects.all()
    serializer_class = LakeOrPondSerializer


class LakeOrPond1827APIView(generics.ListAPIView):
    queryset = LakeOrPond.objects.filter(year="1827")
    serializer_class = LakeOrPondSerializer
    

class LakeOrPond1884APIView(generics.ListAPIView):
    queryset = LakeOrPond.objects.filter(year="1884")
    serializer_class = LakeOrPondSerializer
    

class LakeOrPond2009APIView(generics.ListAPIView):
    queryset = LakeOrPond.objects.filter(year="2009")
    serializer_class = LakeOrPondSerializer

# Widoki dla budynków
class BuildingAPIView(generics.ListAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class Building1827APIView(generics.ListAPIView):
    queryset = Building.objects.filter(year="1827")
    serializer_class= BuildingSerializer
    

class Building1884APIView(generics.ListAPIView):
    queryset = Building.objects.filter(year="1884")
    serializer_class= BuildingSerializer
    

class Building2009APIView(generics.ListAPIView):
    queryset = Building.objects.filter(year="2009")
    serializer_class= BuildingSerializer

# Widoki dla zabudowy zwartej
class CompactSettlementAPIView(generics.ListAPIView):
    queryset = CompactSettlement.objects.all()
    serializer_class = CompactSettlementSerializer


class CompactSettlement1827APIView(generics.ListAPIView):
    queryset = CompactSettlement.objects.filter(year="1827")
    serializer_class = CompactSettlementSerializer


class CompactSettlement1884APIView(generics.ListAPIView):
    queryset = CompactSettlement.objects.filter(year="1884")
    serializer_class = CompactSettlementSerializer


class CompactSettlement2009APIView(generics.ListAPIView):
    queryset = CompactSettlement.objects.filter(year="2009")
    serializer_class = CompactSettlementSerializer

# Widoki dla lasów
class ForestAPIView(generics.ListAPIView):
    queryset = Forest.objects.all()
    serializer_class = ForestSerializer


class Forest1827APIView(generics.ListAPIView):
    queryset = Forest.objects.filter(year="1827")
    serializer_class = ForestSerializer
    

class Forest1884APIView(generics.ListAPIView):
    queryset = Forest.objects.filter(year="1884")
    serializer_class = ForestSerializer
    

class Forest2009APIView(generics.ListAPIView):
    queryset = Forest.objects.filter(year="2009")
    serializer_class = ForestSerializer

# Widoki dla łąk i pastwisk
class MeadowOrPastureAPIView(generics.ListAPIView):
    queryset = MeadowOrPasture.objects.all()
    serializer_class = MeadowOrPastureSerializer


class MeadowOrPasture1827APIView(generics.ListAPIView):
    queryset = MeadowOrPasture.objects.filter(year="1827")
    serializer_class = MeadowOrPastureSerializer


class MeadowOrPasture1884APIView(generics.ListAPIView):
    queryset = MeadowOrPasture.objects.filter(year="1884")
    serializer_class = MeadowOrPastureSerializer


class MeadowOrPasture2009APIView(generics.ListAPIView):
    queryset = MeadowOrPasture.objects.filter(year="2009")
    serializer_class = MeadowOrPastureSerializer

# Widoki dla pozostałych obszarów
class OtherTypeAPIView(generics.ListAPIView):
    queryset = OtherType.objects.all()
    serializer_class = OtherTypeSerializer


class OtherType1827APIView(generics.ListAPIView):
    queryset = OtherType.objects.filter(year="1827")
    serializer_class = OtherTypeSerializer
    

class OtherType1884APIView(generics.ListAPIView):
    queryset = OtherType.objects.filter(year="1884")
    serializer_class = OtherTypeSerializer
    

class OtherType2009APIView(generics.ListAPIView):
    queryset = OtherType.objects.filter(year="2009")
    serializer_class = OtherTypeSerializer


class MultiOtherTypeAPIView(generics.ListAPIView):
    queryset = MultiOtherType.objects.all()
    serializer_class = MultiOtherTypeSerializer


class MultiOtherType1827APIView(generics.ListAPIView):
    queryset = MultiOtherType.objects.filter(year="1827")
    serializer_class = MultiOtherTypeSerializer


class MultiOtherType1884APIView(generics.ListAPIView):
    queryset = MultiOtherType.objects.filter(year="1884")
    serializer_class = MultiOtherTypeSerializer


class MultiOtherType2009APIView(generics.ListAPIView):
    queryset = MultiOtherType.objects.filter(year="2009")
    serializer_class = MultiOtherTypeSerializer

# Widoki dla rzek
class RiverAPIView(generics.ListAPIView):
    queryset = River.objects.all()
    serializer_class = RiverSerializer


class River1827APIView(generics.ListAPIView):
    queryset = River.objects.filter(year="1827")
    serializer_class = RiverSerializer


class River1884APIView(generics.ListAPIView):
    queryset = River.objects.filter(year="1884")
    serializer_class = RiverSerializer


class River2009APIView(generics.ListAPIView):
    queryset = River.objects.filter(year="2009")
    serializer_class = RiverSerializer

# Widoki dla dróg
class RoadAPIView(generics.ListAPIView):
    queryset = Road.objects.all()
    serializer_class = RoadSerializer


class Road1827APIView(generics.ListAPIView):
    queryset = Road.objects.filter(year="1827")
    serializer_class = RoadSerializer


class Road1884APIView(generics.ListAPIView):
    queryset = Road.objects.filter(year="1884")
    serializer_class = RoadSerializer


class Road2009APIView(generics.ListAPIView):
    queryset = Road.objects.filter(year="2009")
    serializer_class = RoadSerializer


class HighwayFieldAPIView(generics.ListAPIView):
    queryset = HighwayField.objects.all()
    serializer_class = HigwayFieldSerializer
