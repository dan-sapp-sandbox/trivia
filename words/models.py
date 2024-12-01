from django.db import models

class Word(models.Model):
    name = models.CharField(max_length=255)
    definition = french = models.TextField()
    french = models.TextField()
    german = models.TextField()
    spanish = models.TextField()
    japanese = models.TextField()

    def __str__(self):
        return self.name
