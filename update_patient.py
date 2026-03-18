import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic.settings')
django.setup()

from appointments.models import Patient

try:
    patient = Patient.objects.get(id=1)
    print(f'Before: {patient.name}')
    patient.name = 'dessa'
    patient.save()
    print(f'After: {patient.name}')
    print("Patient name updated successfully!")
except Patient.DoesNotExist:
    print("Patient with ID 1 not found")
except Exception as e:
    print(f"Error: {e}")
