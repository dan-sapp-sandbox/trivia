from django.db import models

class Song(models.Model):
    name = models.CharField(max_length=255)
    artist = models.TextField()
    release_year = models.TextField()

    def __str__(self):
        return self.name
