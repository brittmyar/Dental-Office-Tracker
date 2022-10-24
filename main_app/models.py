from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age =  models.IntegerField()
    allergies = models.CharField(max_length=100) 
    insurance = models.CharField(max_length=100)

def __str__(self):
        return self.name
    