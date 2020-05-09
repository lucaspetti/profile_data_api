from rest_framework import serializers

from.models import Skill
from.models import App
from.models import Album

class SkillSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Skill
    fields = ('name', 'level')

class AppSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = App
    fields = ('name', 'description')

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Album
    fields = ('name', 'url')
