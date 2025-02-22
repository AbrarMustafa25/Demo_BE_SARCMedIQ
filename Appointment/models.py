from django.db import models
from Patient.models import Patient

# Create your models here.
class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name="patient_visit")
    date = models.DateField()
    reason = models.CharField(max_length=400)

