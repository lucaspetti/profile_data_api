from django.shortcuts import render

from rest_framework import viewsets

from .serializers import SkillSerializer
from .serializers import AppSerializer
from .serializers import AlbumSerializer

from .models import Skill
from .models import App
from .models import Album

class SkillViewSet(viewsets.ModelViewSet):
  queryset = Skill.objects.all().order_by('level')
  serializer_class = SkillSerializer

class AppViewSet(viewsets.ModelViewSet):
  queryset = App.objects.all().order_by('name')
  serializer_class = AppSerializer

class AlbumViewSet(viewsets.ModelViewSet):
  queryset = Album.objects.all().order_by('year')
  serializer_class = AlbumSerializer