from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['package', 'number_of_seats']  # Removed 'customer_name' and 'customer_email'
        widgets = {
            'package': forms.Select(attrs={'class': 'form-control'}),
            'number_of_seats': forms.NumberInput(attrs={'class': 'form-control'}),
        }
