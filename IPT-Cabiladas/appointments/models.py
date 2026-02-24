from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    def __str__(self):
        return f"{self.patient} - {self.doctor}"
