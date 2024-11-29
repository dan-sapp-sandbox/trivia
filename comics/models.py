from django.db import models

class Superhero(models.Model):
    """Model to store superhero information."""
    name = models.CharField(max_length=255)
    power = models.TextField()
    debut_date = models.TextField()
    debut_issue = models.TextField()
    is_villain = models.BooleanField(default=False)
    is_marvel = models.BooleanField(default=False)

    def __str__(self):
        return self.name
