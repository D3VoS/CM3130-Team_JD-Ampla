from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from Accounts.models import User
from .models import event
from .forms import createSession

# Create your views here.
def calendar(request):
    return render(request, 'calendar.html')

def session(request):

    newEvent = createSession()

    context = {'form' : newEvent}

    return render(request, 'session.html', context)

@require_POST
def createEvent(request):
    newEvent = createSession(request.POST)

    if newEvent.is_valid():
        newEvent.save()

    return redirect('session.html')