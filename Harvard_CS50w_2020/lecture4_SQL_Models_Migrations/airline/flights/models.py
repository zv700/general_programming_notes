from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)   # each airport will be identified by a 3 letter abbriviated code name "JFK"
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})" # returns "New York (JFK)"

class Flight(models.Model):     # a Django model = a class, one class per table
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")        #ForeignKey references another table for first argument (in this case Airport), with additional arguments. on_delete --> if you have related tables, SQL needs to know what happens when you delete something. models.CASCADE --> if you delete an airport code, SQL will automatically delete flights related to that airport # provide all of the properties your model/a flight would have that you want to keep track of || related_name --> can search for all rows with same column value [If you have one row with the origin column value: New York, you can sort by all rows that have the same New York value as their origin "every flight departing from NY"]
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")   # variables correspond to SQL table columns
    duration = models.IntegerField()
    
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"   # when called, string will represent the row of data --> '1: New York to London' when id = 1, origin = 'New York' , and destination = 'London'
    
class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")
    
    def __str__(self):
        return f"{self.first} {self.last}"