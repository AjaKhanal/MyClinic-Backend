from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .management.commands.data import *


# Create your views here.
def patient_view(request):
    return JsonResponse({'patients': patients})


def doctor_view(request):
    return JsonResponse({'doctors': doctors})


def clinic_view(request):
    return JsonResponse({'clinics': clinics})


def appointment_view(request):
    return JsonResponse({'appointments': appointments})
