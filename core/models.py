from django.db import models

# Create your models here.
class Patient(models.Model):
    ohip_id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=30)
    dob = models.DateField()
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=6)
    clinic_id = models.ForeignKey(
        'Clinic',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['ohip_id']


class Doctor(models.Model):
    cpso_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    clinic_id = models.ForeignKey(
        'Clinic',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['cpso_id']


class Clinic(models.Model):
    clinic_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    days = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    class Meta:
        ordering = ['clinic_id']


class Appointment(models.Model):
    clinic_id = models.ForeignKey(
        'Clinic',
        on_delete=models.CASCADE,
    )
    cpso_id = models.ForeignKey(
        'Doctor',
        on_delete=models.CASCADE,
    )
    ohip_id = models.ForeignKey(
        'Patient',
        on_delete=models.CASCADE,
    )

    class Types(models.TextChoices):
        full_checkup = "full checkup"
        vitals_checkup = "vitals checkup"
        vaccination = "vaccination"
        prescription_refill = "prescription refill"
        general_consultation = "general consultation"
        other = "other"

    appointment_type = models.CharField(max_length=30, choices=Types.choices)
    start_time = models.CharField(max_length=10)
    end_time = models.CharField(max_length=10)
    date = models.DateField()
    duration = models.IntegerField(default=0)
    address = models.CharField(max_length=100, default="")

    class Meta:
        ordering = ['id']
