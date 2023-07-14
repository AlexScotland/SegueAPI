from django.urls import path, include
from rest_framework.routers import DefaultRouter
from importer.api.viewsets.song_importer import ImportSegueViewSet

router = DefaultRouter()
router.register(r'importer', ImportSegueViewSet, basename="segue_importer")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api/', include(router.urls)),
]