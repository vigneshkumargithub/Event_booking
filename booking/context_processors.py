from .models import Event
from django.utils.timezone import now

def next_event(request):
    upcoming = Event.objects.filter(date__gte=now(), soldout=False).order_by('date').first()
    return {'next_upcoming_event': upcoming}
 