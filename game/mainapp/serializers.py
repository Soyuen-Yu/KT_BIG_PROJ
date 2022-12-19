from rest_framework import serializers
from .models import Shop, Item

class ItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = Item
    fields = '__all__'

class ShopSerializer(serializers.ModelSerializer):
  item = ItemSerializer(read_only=True)

  class Meta:
    model = Shop
    fields = '__all__'