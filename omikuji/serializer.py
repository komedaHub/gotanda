from rest_framework import serializers

from .models import Omikuji, Omikuji_items

class OmikujiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Omikuji
        fields = ('name','created_at')

class OmikujiItemSerializer(serializers.ModelSerializer):
    omikuji = OmikujiSerializer()
    class Meta:
        model = Omikuji_items
        fields = ('omikuji', 'item_name')
