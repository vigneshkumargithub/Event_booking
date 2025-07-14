from django.contrib import admin
from .models import Event, Booking, CustomUser
from django.contrib.auth.admin import UserAdmin

class EventAdmin(admin.ModelAdmin):
    list_display=("id","title","description","date","capacity","soldout")

class BookingAdmin(admin.ModelAdmin):
    list_display=("event","name","email","number_of_seats")



admin.site.register(Event, EventAdmin)
admin.site.register(Booking,BookingAdmin)
admin.site.register(CustomUser, UserAdmin)
