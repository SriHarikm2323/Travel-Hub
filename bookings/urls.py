from django.urls import path
from . import views

urlpatterns = [
    path('', views.travel_packages, name='travel_packages'),
    path('book/<int:package_id>/', views.book_package, name='book_package'),
    path('bookings/', views.bookings_list, name='bookings_list'),
    path('bookings/search', views.search, name='search'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('packages/<int:package_id>/', views.package_details, name='package_details'),
    
]


