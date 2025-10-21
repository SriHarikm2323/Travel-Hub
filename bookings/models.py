from django.db import models
from django.contrib.auth import get_user_model

class TravelPackage(models.Model):
    title = models.CharField(max_length=200)
    destination = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.PositiveIntegerField()
    image = models.ImageField(upload_to='packages/', blank=True, null=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    package = models.ForeignKey(TravelPackage, on_delete=models.CASCADE)
    number_of_seats = models.PositiveIntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)

    def __str__(self):
        package_title = self.package.title if self.package else "Unknown Package"
        username = self.user.username if self.user else "Unknown User"
        return f"Booking for {package_title} by {username}"
