from django.contrib import admin
from .models import TravelPackage, Booking
from django.contrib import admin
from .models import TravelPackage

from django.contrib import admin
from .models import TravelPackage

@admin.register(TravelPackage)
class TravelPackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'destination', 'price', 'available_seats')  # Fields in list view
    search_fields = ('title', 'destination')
    list_filter = ('destination',)
    fields = ('title', 'destination', 'description', 'price', 'available_seats', 'image')  # Include image in form


admin.site.register(Booking)
