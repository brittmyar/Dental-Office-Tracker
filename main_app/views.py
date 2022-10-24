from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Patient, Provider
from .forms import ProcedureForm
# Define the home view
def home(request):
  return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

# Add new view
def patients_index(request):
    patients = Patient.objects.all()
    return render(request, 'patients/index.html', { 'patients': patients })


def patients_detail(request, patient_id):
  patient = Patient.objects.get(id=patient_id)
  providers_patient_doesnt_have = Provider.objects.exclude(id__in = patient.providers.all().values_list('id'))
  procedure_form = ProcedureForm()
  return render(request, 'patients/detail.html', {
    'patient': patient, 
    'procedure_form': procedure_form,
    'providers': providers_patient_doesnt_have
  })

def add_procedure(request, patient_id):
    form = ProcedureForm(request.POST)
    if form.is_valid():
        new_procedure = form.save(commit=False)
        new_procedure.patient_id = patient_id
        new_procedure.save()
    return redirect('detail', patient_id=patient_id)

def assoc_provider(request, patient_id, provider_id):
   Patient.objects.get(id=patient_id).providers.add(provider_id)
   return redirect('detail', patient_id=patient_id)

class PatientCreate(CreateView):
    model = Patient
    fields = '__all__'
    success_url = '/patients/'


class PatientUpdate(UpdateView):
  model = Patient
  fields = ['age', 'allergies', 'insurance']

class PatientDelete(DeleteView):
    model = Patient
    success = '/patients/'