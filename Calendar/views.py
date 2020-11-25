from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from Accounts.models import User
from .models import event
from .forms import createSession

# Create your views here.
def calendar(request):
    return render(request, 'calendar.html')

def session(request):
    form  = createSession(request.POST or None)
    if form.is_valid():
        form.save()

    context =  {
        'form': form
    }
    return render(request, 'session.html', context)