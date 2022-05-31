from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('person/<int:person_id>', views.person, name='person'),
    path('flight/<int:flight_id>', views.flight, name='flight'),
]