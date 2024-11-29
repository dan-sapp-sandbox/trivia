from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255)
    actors = models.TextField()
    release_year = models.TextField()

    def __str__(self):
        return self.name
