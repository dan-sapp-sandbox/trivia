from django.db import models

class Landmark(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.TextField()
    longitude = models.TextField()

    def __str__(self):
        return self.name
