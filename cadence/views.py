from django.shortcuts import render
from django.http import HttpResponse


def Cadence(request):
    cadence = [
        {'id':1, 'name': 'Yomi Succinct', 'age': 20}
    ]
    return HttpResponse(cadence)

# Create your views here.
