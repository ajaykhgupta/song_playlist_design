from django.db import models
from django.shortcuts import render
from rest_framework.utils import serializer_helpers
from .serializers import SongSerializer
from .models import songlist
from rest_framework import generics, serializers
# Create your views here.

class ListSong(generics.ListAPIView):
    queryset = songlist.objects.all()
    serializer_class = SongSerializer

class DetailList(generics.RetrieveAPIView):
    queryset = songlist.objects.all()
    serializer_class = SongSerializer

