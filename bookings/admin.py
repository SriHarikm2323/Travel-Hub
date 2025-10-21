from django.contrib import admin
from .models import TravelPackage, Booking

@admin.register(TravelPackage)
class TravelPackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'destination', 'price', 'available_seats')  # Fields in list view
    search_fields = ('title', 'destination')
    list_filter = ('destination',)
    fields = ('title', 'destination', 'description', 'price', 'available_seats', 'image')  # Include image in form

class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'user_username', 
        'user_email', 
        'package', 
        'number_of_seats', 
        'booking_date'
    )
    search_fields = ('user__username', 'user__email', 'package__title')
    list_filter = ('booking_date', 'package')

    def user_username(self, obj):
        return obj.user.username if obj.user else "Unknown User"
    user_username.short_description = 'User'

    def user_email(self, obj):
        return obj.user.email if obj.user else "No Email"
    user_email.short_description = 'Email'

admin.site.register(Booking, BookingAdmin)
