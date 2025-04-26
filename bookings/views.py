from django.shortcuts import render, redirect
from .models import TravelPackage, Booking
from .forms import BookingForm

# View travel packages
def travel_packages(request):
    packages = TravelPackage.objects.all()
    return render(request, 'bookings/travel_packages.html', {'packages': packages})

# Book a travel packagedef
def book_package(request, package_id):
    package = TravelPackage.objects.get(id=package_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('travel_packages')
    else:
        form = BookingForm(initial={'package': package})

    return render(request, 'bookings/book_package.html', {'form': form, 'package': package})
# View all bookings (admin)
def bookings_list(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings/bookings_list.html', {'bookings': bookings})
def travel_packages(request):
    query = request.GET.get('query','')  # Get the query parameter from the URL
    if query:
        packages = TravelPackage.objects.filter(title__icontains=query)  # Filter packages by query
    else:
        packages = TravelPackage.objects.all()  # If no query, show all packages
    return render(request, 'bookings/travel_packages.html', {'packages': packages, 'query':query})

from django.shortcuts import render
from django.db.models import Q
from .models import TravelPackage

def search(request):
    query = request.GET.get('query', '')  # Get the query parameter from the URL
    if query:
        packages = TravelPackage.objects.filter(
            Q(title__icontains=query) | Q(destination__icontains=query)
        )  # Filter packages by title or destination
    else:
        packages = TravelPackage.objects.all()  # If no query, show all packages
    return render(request, 'bookings/search.html', {'packages': packages, 'query': query})

    

def about_us(request): 
    return render(request, 'bookings/about_us.html')
def contact_us(request): 
    return render(request, 'bookings/contact_us.html')

def package_details(request, package_id):
    package = Package.objects.get(id=package_id)
    return render(request, 'search.html', {'package': package})


