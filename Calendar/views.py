from django.shortcuts import render
from datetime import date, datetime

from .models import event
from Accounts.models import User
from .forms import createSession, bookingEvent

# Create your views here.
def calendar(request):
    return render(request, 'calendar.html')

def session(request):
    user = request.user
    
    events = event.objects.filter(eventDate__gte = date.today()).order_by('eventDate')
    
    form  = createSession(request.POST or None, initial = {'eventCreator': user} )

    if request.method == 'POST' and 'create' in request.POST:
        if form.is_valid():
            form.save(form.cleaned_data)

    context =  {
        'form': form,
        'events': events,
        'user': user
    }

    if request.method == 'POST' and "join" in request.POST :
        if request.POST.get('bookingUser') and request.POST.get('bookingEventID'):
            book=bookingEvent()
            book.bookingEventID = event.objects.get(id = request.POST.get('bookingEventID'))
            book.bookingUser = User.objects.get(id = request.POST.get('bookingUser'))
            book.save()

    return render(request, 'session.html', context)

    