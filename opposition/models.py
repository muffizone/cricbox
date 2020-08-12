from django.db import models

# Create your models here.
class Opposition(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
