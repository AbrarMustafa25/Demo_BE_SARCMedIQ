from django.contrib import admin
from .models import Visit

# Register your models here.
# ==========================================================================
class VisitAdmin(admin.ModelAdmin):
    list_display = ['patient', 'date', 'reason']
    list_filter = ['date', 'reason']
    search_fields = ['date', 'reason']

admin.site.register(Visit, VisitAdmin)
