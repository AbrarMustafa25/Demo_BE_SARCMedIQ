from django.db import models

# Create your models here.
class Patient(models.Model):
    mr_number = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    date_of_birth = models.DateField(null=True, blank=True)

