from django.contrib import admin
from .models import Patient

# Register your models here.
# ==========================================================================
class PatientAdmin(admin.ModelAdmin):
    list_display = ['mr_number', 'first_name', 'last_name', 'date_of_birth']
    list_filter = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']

admin.site.register(Patient, PatientAdmin)
