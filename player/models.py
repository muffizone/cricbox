from django.db import models


# Create your models here.
class Player(models.Model):
    full_name = models.CharField(max_length=50, primary_key=True)
    member_since = models.DateField("date joined", null=True, blank=True)

    class Meta:
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name
