from rest_framework import serializers
from .models import Visit
from Patient.serializers import PatientSerializer

class VisitSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)

    class Meta:
        model = Visit
        fields = '__all__'
