from rest_framework import serializers
from .models import Event, Booking

class EventSerializer(serializers.ModelSerializer):
    seats_left = serializers.IntegerField( read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'capacity', 'soldout', 'seats_left']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'name', 'email', 'number_of_seats', 'event']
