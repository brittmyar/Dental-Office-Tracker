
from django.forms import ModelForm
from .models import Procedure

class ProcedureForm(ModelForm):
  class Meta:
    model = Procedure
    fields = ['date', 'type', 'location']
