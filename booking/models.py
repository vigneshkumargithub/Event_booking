from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    capacity = models.PositiveBigIntegerField()
    soldout = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def booked_seats(self):
        return sum(booking.number_of_seats for booking in self.bookings.all())
    
    def seats_left(self):
        return self.capacity - self.booked_seats()
    


class Booking(models.Model):
    event = models.ForeignKey(Event, related_name='bookings', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number_of_seats =models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.event.title}"
    
