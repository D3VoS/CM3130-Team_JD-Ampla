from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from .models import Contact
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

@login_required
def contact(request):
    form = ContactForm(creator=request.user, data=request.POST or None)
    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact Form Submitted')
            return redirect('Core:index')
    except Exception as e:
        #Displays an error message
        print(e)
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)

def admin_index(request):
    items = Contact.objects.all()
    context = {"items": items}
    print(len(context['items']))
    return render(request, 'admin_index.html', context)