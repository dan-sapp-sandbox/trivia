from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.TextField()
    release_year = models.TextField()

    def __str__(self):
        return self.name

