import json
from segue_api.models.Songs import Songs
class SongJSONImporter():

    def __init__(self, song_json):
        self.import_song(song_json)
    
    def import_song(self, json):
        for album in json.get("albums"):
            song_artist = album.get("artist")
            for track in album.get("tracks"):
                song = track.split("/")
                song_name = song[0].strip()
                segued_song_name = song[1].strip()
                if Songs.objects.filter(song_name= segued_song_name, artist_name= song_artist).exists():
                    segued_song = Songs.objects.get(song_name= segued_song_name, artist_name= song_artist)
                else:
                    segued_song = Songs(song_name= segued_song_name, artist_name= song_artist)                         
                    segued_song.save()
                if Songs.objects.filter(song_name= song_name, artist_name= song_artist).exists():
                    original = Songs.objects.get(song_name= segued_song_name, artist_name= song_artist)
                    original.segued_song = segued_song
                    original.save()
                else:
                    original = Songs(song_name= song_name, artist_name= song_artist, segued_song= segued_song)
                    original.save()

