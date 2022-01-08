from django.db.models import fields
from rest_framework import serializers
from .models import songlist

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = songlist
        fields = ('__all__')