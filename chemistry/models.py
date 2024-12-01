from django.db import models

class Element(models.Model):
    name = models.CharField(max_length=255)
    number = models.TextField()
    symbol = models.TextField()

    def __str__(self):
        return self.name