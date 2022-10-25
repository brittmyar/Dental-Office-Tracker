from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('patients/', views.patients_index, name='index'),
    path('patients/<int:patient_id>/', views.patients_detail, name='detail'),
    path('patients/create/', views.PatientCreate.as_view(), name='patients_create'),
    path('patients/<int:pk>/update/',
         views.PatientUpdate.as_view(), name='patients_update'),
    path('patients/<int:pk>/delete/',
         views.PatientDelete.as_view(), name='patients_delete'),
    path('patients/<int:patient_id>/add_procedure/', views.add_procedure, name='add_procedure'),
    path('providers/', views.ProviderList.as_view(), name='providers_index'),
    path('providers/<int:pk>/', views.ProviderDetail.as_view(), name='providers_detail'),
    path('providers/create/', views.ProviderCreate.as_view(), name='providers_create'),
    path('providers/<int:pk>/update/', views.ProviderUpdate.as_view(), name='providers_update'),
    path('providers/<int:pk>/delete/', views.ProviderDelete.as_view(), name='providers_delete'),
    path('patients/<int:patient_id>/assoc_provider/<int:provider_id>/', views.assoc_provider, name='assoc_provider'),
    path('accounts/signup/', views.signup, name='signup'),
]
