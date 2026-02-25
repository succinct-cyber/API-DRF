from django.db import models

class Cadence(models.Model):
    Cadence_id = models.CharField(max_length=10)
    name = models.TextField(max_length=50)
    branch = models.CharField(max_length=20)

    def __str__ (self):
        return self.name