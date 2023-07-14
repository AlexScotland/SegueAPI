from django.db import models


class Songs(models.Model):
    song_name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    segued_song = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)