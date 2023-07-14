from django.urls import path, include
from rest_framework.routers import DefaultRouter
from segue_api.api.viewsets.segue_song import SegueViewSet

router = DefaultRouter()
router.register(r'songs', SegueViewSet, basename="segue_song")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api/', include(router.urls)),
]