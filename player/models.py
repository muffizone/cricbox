from django.db import models


# Create your models here.
# class PlayerAppearances(models.manager):
#
#     def get_queryset(self):
#         return super().get_queryset().values('full_name').


class Player(models.Model):
    full_name = models.CharField(max_length=50, primary_key=True)
    member_since = models.DateField("Date Joined", null=True, blank=True)
    email = models.EmailField("Email", null=True, blank=True)

    class Meta:
        ordering = ["full_name"]
        db_table = "players"

    def __str__(self):
        return self.full_name
