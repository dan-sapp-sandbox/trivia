from django.db import models

class Superhero(models.Model):
    name = models.CharField(max_length=255)
    alias = models.TextField(default="")
    power = models.TextField()
    debut_date = models.TextField()
    debut_issue = models.TextField()
    is_villain = models.BooleanField(default=False)
    is_marvel = models.BooleanField(default=False)
    teams = models.TextField(default="")

    def __str__(self):
        return self.name
