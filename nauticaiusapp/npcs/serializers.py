from rest_framework import serializers
from .models import Npc

class NpcSerializer(serializers.ModelSerializer):

    class Meta:
        model = Npc
        fields = ('id', 'name', 'race', 'class_field', 'age', 'height', 'alignment', 'affiliation', 'first_appearance', 'str', 'dex', 'con', 'int', 'wis', 'cha', 'description')
