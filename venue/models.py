from django.db import models

# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    location = models.URLField("Google maps link to the venue", blank=True)

    def __str__(self):
        return self.name

