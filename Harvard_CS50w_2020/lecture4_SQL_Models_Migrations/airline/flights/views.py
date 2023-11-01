from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


from .models import Flight, Passenger

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

# index page displays a list of all flights when a request is made to render/view the page --> import the table containing the flight data [Flight] to be able to display all of the flight data
# all flight data from Flight model/table are represented by Flight.objects.all() --> flight data is the VALUE stored within the KEY/variable: "flights"  
# needs html templates to be able to display the page --> flights/templates/flights/layout.html and index.html
# /flights is a view that can be accessed by placing at the end of the url when you runserver

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,   # which flight is being rendered
        "passengers": flight.passengers.all(),  # who is booked to the flight
        "non_passengers": Passenger.objects.exclude(flights=flight).all()    # query for all passengers EXCEPT for passengers who are already on the flight
    })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))   # an input field. string in square brackets ["inputFieldName"] determines what name will be recieved when this book route is able to process the POST request. The input might be a string by default, so convert to an integer with int()
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id, )))