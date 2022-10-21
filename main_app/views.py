from django.shortcuts import render, redirect
from django.http import HttpResponse

# Define the home view
def home(request):
  return render('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')