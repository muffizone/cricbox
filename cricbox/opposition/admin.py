from .models import Opposition

# Django imports
from django.contrib import admin


# Register your models here.
class OppositionAdmin(admin.ModelAdmin):
    list_display = ["name", "site"]
    search_fields = ["name"]


admin.site.register(Opposition, OppositionAdmin)
