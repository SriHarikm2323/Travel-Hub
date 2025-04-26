from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['package', 'customer_name', 'customer_email', 'number_of_seats']
        widgets = {
            'package': forms.Select(attrs={'class': 'form-control'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'number_of_seats': forms.NumberInput(attrs={'class': 'form-control'}),
        }
