from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from segue_api.models.Songs import Songs

class SegueViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """

    @action(detail=False, methods=['post'])
    def get_valid_segue_from_song_and_artist(self, request):
        requested_song = request.data.get("song", None)
        requested_artist = request.data.get("artist", None)
        # Get Song From Database Using Artist String and Song Name
        if Songs.objects.filter(song_name=requested_song, artist_name=requested_artist).exists():
            song_requested = Songs.objects.get(song_name=requested_song, artist_name=requested_artist)
            if song_requested.segued_song:
                segued_song = Songs.objects.get(song_name=requested_song, artist_name=requested_artist).segued_song
                return Response(data ={"song": segued_song.song_name, "artist":segued_song.artist_name})
            else:
                return Response("No Segue", 400)
        return Response("Song Not found", 400)