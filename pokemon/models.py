from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=255)
    types = models.TextField()
    gen_of_first_appearance = models.TextField()

    def __str__(self):
        return self.name
