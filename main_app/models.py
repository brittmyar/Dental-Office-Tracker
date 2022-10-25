from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

PROCEDURES = (
    ('R', 'Root Canal'),
    ('C', 'Cleaning'),
    ('F', 'Filling'),
    ('E', 'Extraction'),
    ('B', 'BiteWings'),
    ('P', 'Panoramic')
)

class Provider(models.Model):
    name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('providers_detail', kwargs={'pk': self.id})

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age =  models.IntegerField()
    allergies = models.CharField(max_length=100) 
    insurance = models.CharField(max_length=100)
    providers = models.ManyToManyField(Provider)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'patient_id': self.id})

class Procedure(models.Model):
    date = models.DateField('Procedure Date')
    type = models.CharField( 
        max_length=1,
        choices=PROCEDURES,
        default=PROCEDURES[0][0]
        
        )
    location = models.CharField(max_length=100)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_type_display()} on {self.date}"

class Meta:
    ordering = ['-date']