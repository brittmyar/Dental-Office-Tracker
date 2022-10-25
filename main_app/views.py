from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Patient, Provider
from .forms import ProcedureForm
# Define the home view
def home(request):
  return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def patients_index(request):
    patients = Patient.objects.filter(user=request.user)
    return render(request,'patients/index.html', { 'patients': patients})


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

# Add new view
def patients_index(request):
    patients = Patient.objects.filter(user=request.user)
    return render(request, 'patients/index.html', { 'patients': patients })


def patients_detail(request, patient_id):
  patient = Patient.objects.get(id=patient_id)
  procedure_form = ProcedureForm()


  providers_patient_doesnt_have = Provider.objects.exclude(id__in = patient.providers.all().values_list('id'))
  
  return render(request, 'patients/detail.html', {
    'patient': patient, 
    'procedure_form': procedure_form,
    'providers': providers_patient_doesnt_have,
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

class PatientCreate(LoginRequiredMixin, CreateView):
    model = Patient
    fields = ['name', 'age', 'allergies', 'insurance']
    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user 
        return super().form_valid(form)

class PatientUpdate(UpdateView):
  model = Patient
  fields = ['age', 'allergies', 'insurance']

class PatientDelete(DeleteView):
    model = Patient
    success = '/patients/'

class ProviderCreate(CreateView):
    model = Provider
    fields = ('name',)

class ProviderUpdate(UpdateView):
    model = Provider
    fields = ('name',)

class ProviderDelete(DeleteView):
    model = Provider
    success_url = '/providers/'

class ProviderDetail(DetailView):
    model = Provider
    template_name = 'providers/detail.html'

class ProviderList(ListView):
    model = Provider
    template_name = 'providers/index.html'