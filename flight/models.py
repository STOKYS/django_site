from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Passenger(models.Model):
    seat = models.IntegerField()
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.flight} / {self.person} [{self.seat}]'


class Staff(models.Model):
    role = models.CharField(max_length=45)
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.flight} / {self.person} [{self.role}]'


class Gender(models.TextChoices):
    MALE = "Male",
    FEMALE = "Female"


class Person(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    gender = models.CharField(max_length=6, choices=Gender.choices, default=Gender.MALE)
    date_of_birth = models.DateField()
    postcode = models.CharField(max_length=45)
    street_name = models.CharField(max_length=45)
    house_number = models.IntegerField()
    city = models.ForeignKey('City', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Plane(models.Model):
    model = models.CharField(max_length=45)
    no_of_seats = models.IntegerField()

    def __str__(self):
        return self.model


class Airport(models.Model):
    name = models.CharField(max_length=45)
    city = models.ForeignKey('City', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Flight(models.Model):
    price = models.DecimalField(max_digits=32, decimal_places=2)
    terminal = models.IntegerField()
    date = models.DateTimeField()
    plane = models.ForeignKey('Plane', on_delete=models.CASCADE)
    start = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name='hey')
    destination = models.ForeignKey('Airport', on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.date}] - {self.start} : {self.destination}'