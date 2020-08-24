from django.contrib import admin
from .models import Opposition


# Register your models here.
class OppositionAdmin(admin.ModelAdmin):
    list_display = ["name", "site"]
    search_fields = ["name"]


admin.site.register(Opposition, OppositionAdmin)
