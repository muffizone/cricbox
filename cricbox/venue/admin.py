from .models import Venue

# Django imports
from django.contrib import admin


# Register your models here.
class VenueAdmin(admin.ModelAdmin):
    list_display = ["name", "location"]
    search_fields = ["name"]


admin.site.register(Venue, VenueAdmin)
