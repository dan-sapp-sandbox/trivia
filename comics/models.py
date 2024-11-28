from django.db import models

class Superhero(models.Model):
    """Model to store superhero information."""
    name = models.CharField(max_length=255)
    power = models.TextField()
    debut_date = models.TextField()
    debut_issue = models.TextField()

    def __str__(self):
        return self.name
