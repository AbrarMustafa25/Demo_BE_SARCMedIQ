from django.db import models, IntegrityError
from Patient.models import Patient

class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name="patient_visit")
    date = models.DateField()
    reason = models.CharField(max_length=400)

    class Meta:
        unique_together = ('patient', 'date', 'reason')

    # def save(salf, *args, **kwargs):
    #     try:
    #         super.save(*args, **kwargs)
    #         print(str(*args))
    #     except IntegrityError:
    #         raise ""
        