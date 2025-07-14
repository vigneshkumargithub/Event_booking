from django.shortcuts import render,get_object_or_404, redirect
from .models import Event
from .forms import BookingForm
from django.core.mail import send_mail


def event_list(request):
    events = Event.objects.all().order_by('date')
    return render (request, 'booking/event_list.html', {'events':events} )


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.event = event
            if booking.number_of_seats <= event.seats_left():
                booking.save()
                if event.seats_left() <= 0:
                    event.soldout = True
                    event.save()
                send_mail(
                    'Booking Confirmation',
                    f'Hello {booking.name}, your booking for {event.title} is confirmed.',
                    'noreply@example.com',
                    [booking.email],
                )
                return render(request, 'booking/booking_confirmation.html', {'booking': booking})
            else:
                form.add_error('number_of_seats', 'Not enough seats available.')

    return render(request, 'booking/event_detail.html', {'event': event, 'form': form})

def admin_events(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('admin:login')
    events = Event.objects.all()
    return render(request, 'booking/admin_events.html', {'events': events})

