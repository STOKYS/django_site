# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from flight.models import *


def index(request):
    context = {
        'flights': Flight.objects.all(),
        'persons': Person.objects.all(),
    }
    return render(request, 'index.html', context=context)


# def person(request, person_id):
#     context = {
#         'person_filter': Person.objects.filter(id=person_id).values_list(flat=True).distinct(),
#         'person_get': Person.objects.get(pk=person_id)
#     }
#     return render(request, 'page/detail.html', context=context)


def flights(request):
    context = {
        'flights': Flight.objects.all(),
    }
    return render(request, 'page/list.html', context=context)


def flight(request, flight_id):
    context = {
        'flight_filter': Flight.objects.filter(id=flight_id).values_list(flat=True).distinct().first(),
        'flight_get': Flight.objects.get(pk=flight_id),
        'flight_staff': Staff.objects.filter(flight=flight_id),
        'flight_passenger': Passenger.objects.filter(flight=flight_id),
    }
    return render(request, 'flight/detail.html', context=context)


def person(request, person_id):
    context = {
        'person': Person.objects.get(pk=person_id),
        'passengers': Passenger.objects.filter(person=person_id),
        'staffs': Staff.objects.filter(person=person_id)
    }
    return render(request, 'person/person.html', context=context)
