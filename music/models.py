from django.db import models

class Album(models.Model):
    albumTitle = models.CharField(max_length = 100)
    artist = models.CharField(max_length = 100)

    def __str__(self):
        return self.albumTitle

class Track(models.Model):
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    songTitle = models.CharField(max_length = 100)
