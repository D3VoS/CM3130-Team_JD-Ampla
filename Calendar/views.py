from django.shortcuts import render

from .forms import createSession

# Create your views here.
def calendar(request):
    return render(request, 'calendar.html')

def session(request):
    if request.method == 'POST':
        form = createSession(request.POST)
    
    else:
        form = createSession()

    return render(request, 'session.html', {'form': form})