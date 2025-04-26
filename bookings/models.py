from django.db import models

class TravelPackage(models.Model):
    title = models.CharField(max_length=200)
    destination = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.PositiveIntegerField()
    image = models.ImageField(upload_to='packages/', blank=True, null=True)  # New field


    def __str__(self):
        return self.title

class Booking(models.Model):
    package = models.ForeignKey(TravelPackage, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    number_of_seats = models.PositiveIntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.package.title}"
