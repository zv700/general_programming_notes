from django.contrib import admin
                                    # register models to be able to edit them using Django web interface
from .models import Flight, Airport, Passenger # before registering models below, you must import those models from models.py

# Register your models here.
class FlightAdmin(admin.ModelAdmin):    # customize the admin page for the Flight model
	list_display = ('id', 'origin', 'destination', 'duration',) # CURRENTLY NOT WORKING FOR ME after troubleshooting, look into later bc not the most essential feature. "I would like to see these specific columns in the list display on the admin page"

class PassengerAdmin(admin.ModelAdmin):
	filter_horizontal = ("flights",)    # window size needs to be larger or fullscreen to be able to see the "horizontal" aspect of the horizontal filter

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)