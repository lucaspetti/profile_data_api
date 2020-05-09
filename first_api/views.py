from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions

from .serializers import SkillSerializer
from .serializers import AppSerializer
from .serializers import AlbumSerializer

from .models import Skill
from .models import App
from .models import Album

class SkillViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  queryset = Skill.objects.all().order_by('level')
  serializer_class = SkillSerializer

class AppViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  queryset = App.objects.all().order_by('name')
  serializer_class = AppSerializer

class AlbumViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  queryset = Album.objects.all().order_by('year')
  serializer_class = AlbumSerializer