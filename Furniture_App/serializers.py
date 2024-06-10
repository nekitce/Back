from rest_framework import serializers
from Furniture_App.models import Furniture

class FurnitureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Furniture
        fields = ['furniture_name',
                  'count_part',
                  'material',
                  'weight']


