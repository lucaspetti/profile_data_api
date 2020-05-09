from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'skills', views.SkillViewSet)
router.register(r'apps', views.AppViewSet)
router.register(r'albums', views.AlbumViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
