from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import TravelPackage, Booking
from .forms import BookingForm


# View travel packages
@login_required(login_url='login')
def travel_packages(request):
    query = request.GET.get('query', '')
    if query:
        packages = TravelPackage.objects.filter(title__icontains=query)[:3]
    else:
        packages = TravelPackage.objects.all()[:3]
    return render(request, 'bookings/travel_packages.html', {'packages': packages, 'query': query})


# Book a travel package
@login_required(login_url='login')
def book_package(request, package_id):
    package = TravelPackage.objects.get(id=package_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Add the user to the form data before saving
            booking = form.save(commit=False)
            booking.user = request.user  # Associate the booking with the logged-in user
            booking.save()
            return redirect('bookings_list')  # Redirect to the bookings list
    else:
        form = BookingForm(initial={'package': package})

    return render(request, 'bookings/book_package.html', {'form': form, 'package': package})



# View all bookings (admin)
@login_required(login_url='login')
def bookings_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/bookings_list.html', {'bookings': bookings})



# Search view (could be separate or integrated with travel_packages)
@login_required(login_url='login')
def search(request):
    query = request.GET.get('query', '')
    if query:
        packages = TravelPackage.objects.filter(
            Q(title__icontains=query) | Q(destination__icontains=query)
        )
    else:
        packages = TravelPackage.objects.all()
    return render(request, 'bookings/search.html', {'packages': packages, 'query': query})


# Static pages
def about_us(request):
    return render(request, 'bookings/about_us.html')

def contact_us(request):
    return render(request, 'bookings/contact_us.html')


# Package details
def package_details(request, package_id):
    package = TravelPackage.objects.get(id=package_id)
    return render(request, 'search.html', {'package': package})


# Registration view
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return render(request, 'bookings/register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already registered")
                return render(request, 'bookings/register.html')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                messages.success(request, "Registration successful!")
                return redirect('login')
        else:
            messages.info(request, "Passwords do not match")
            return render(request, 'bookings/register.html')
    else:
        return render(request, 'bookings/register.html')


# Login view with user type logic
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_type = request.POST.get('user_type', 'user')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Logged in successfully!')
            if user_type == 'admin':
                return redirect('/admin/')  # You can change this to an actual admin dashboard
            else:
                return redirect('travel_packages')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    return render(request, 'bookings/login.html')


# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')
