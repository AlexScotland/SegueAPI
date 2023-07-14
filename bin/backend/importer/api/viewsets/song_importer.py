from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from importer.models.song_importer_json import SongJSONImporter

class ImportSegueViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """

    def create(self, request):
        imp = SongJSONImporter(request.data)