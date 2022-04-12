# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from flight.models import *


def index(request):
    context = {
        'flights': Flight.objects.all()
    }
    print(context)
    return render(request, 'index.html', context=context)
