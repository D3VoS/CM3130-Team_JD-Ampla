from django.db import connection
from django.shortcuts import render
from datetime import date, datetime
from json import dumps

from .models import event, bookingEvent
from Accounts.models import User
from .forms import createSession

# Create your views here.
def calendar(request):
    user = str(request.user)
    cursor = connection.cursor()
    cursor.execute(
        '''
        SELECT eventName, eventDate, eventStart, eventEnd
        FROM Calendar_bookingevent, Calendar_event, Accounts_user
        WHERE Calendar_event.id = Calendar_bookingevent.bookingEventID_id 
        AND Calendar_bookingevent.bookingUser_id = Accounts_user.id 
        AND Accounts_user.email = %s 
        ''', [user]
        )
    x = cursor.description
    results = cursor.fetchall()
    resultsList = []
    for r in results:
        i = 0
        d = {}
        while i < len(x):
            d[x[i][0]] = r[i]
            i = i+1
        resultsList.append(d)

    bookedEvents = resultsList
    context = {
        "events" : dumps(bookedEvents,  indent=4, sort_keys=True, default=str)
    }
    return render(request, 'calendar.html', context)

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
            book.bookingUser = user
            book.save()

    return render(request, 'session.html', context)

    