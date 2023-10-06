from rest_framework import viewsets
from .serializers import ProgramadorSerializers
from .models import Progamador

# Create your views here.


class Programadorviewset(viewsets.ModelViewSet):
    queryset = Progamador.objects.all()
    serializer_class =  ProgramadorSerializers