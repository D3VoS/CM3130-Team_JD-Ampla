from django.shortcuts import render
from .forms import ContactForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    form = ContactForm(data=request.POST or None)
    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact Form Submitted')
            return redirect('Core:index')
    except Exception as e:
        #Displays an error message
        messages.warning(request, 'Error :(; The specified form could not be submitted. Error {}'.format(e))
    context = {
        'form': form
    }
    return render(request, 'contact.html', context )
    