from rest_framework import serializers
from .models import Progamador

class ProgramadorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Progamador
        #campos = ('full_name', 'last_name', 'age', 'ia_active')
        fields = '__all__'