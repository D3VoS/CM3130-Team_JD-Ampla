from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from .models import Contact
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test



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


@user_passes_test(lambda u: u.is_staff)
def admin_index(request):
    items = Contact.objects.all()
    context = {"items": items}
    return render(request, 'admin_index.html', context)

@user_passes_test(lambda u: u.is_staff)
def findByID(request, id):
    item = Contact.objects.all().filter(id=id)
    print(len(item))
    context = {"items": item}
    return render(request, 'contact_view.html', context)


@user_passes_test(lambda u: u.is_staff)
def archive(request, id):
    item = Contact.objects.filter(id=id).update(active=False)
    return redirect('Core:admin')


def archived_forms(request):
    items = Contact.objects.all()
    context = {"items": items}
    return render(request, 'archived_forms.html', context)