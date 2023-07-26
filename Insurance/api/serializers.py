from rest_framework import serializers
from .models import Insurance


class InsuranceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'