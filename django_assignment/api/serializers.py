from rest_framework import serializers
from .models import Country

class CountrySerializer(serializers.ModelSerializer):
    Name = serializers.ReadOnlyField()
    class Meta:
        model=Country
        fields='__all__'
